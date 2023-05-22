from datasets import load_dataset
import zlib
from io import BytesIO
from level import Level
import random
from kaitaistruct import KaitaiStream
import numpy as np
import tensorflow as tf
from collections import defaultdict

# Global variables to tweak
# nxn context size, choose 3, 5, or 7. Bad output after that
context_size = 5
# First n levels to train on
num_levels = 5000
# Number of samples for each object generally
# Use -1 to have no limit
num_objects_limit = -1
# Whether to train on no object at all/air
include_air = False
# Model name
model_name = "../savedmodel" + str(context_size)
epochs = 30
batch_size = 128

ds = load_dataset("TheGreatRambler/mm2_level", streaming=True, split="train")

MAX_OBJECT_ID = 132
object_choices = defaultdict(lambda: [])
if include_air:
    input_shape = (MAX_OBJECT_ID + 2) * (context_size * context_size - 1)
    output_shape = MAX_OBJECT_ID + 2
else:
    input_shape = (MAX_OBJECT_ID + 1) * (context_size * context_size - 1)
    output_shape = MAX_OBJECT_ID + 1

# Input and output tensors
input_tensors = []
output_tensors = []
obj_distribution = defaultdict(lambda: 0)

# Get possible object choices
counter = 0
for level_info in iter(ds):
    level = Level(KaitaiStream(BytesIO(zlib.decompress(level_info["level_data"]))))
    max_x = 0
    max_y = 0
    for i in range(level.overworld.object_count):
        # Find the max X and Y for objects
        obj = level.overworld.objects[i]
        x = obj.x // 160
        y = obj.y // 160
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    level_grid = np.full((max_x + 1, max_y + 1), -1, dtype=np.int16)
    for i in range(level.overworld.object_count):
        # Assign the objects
        obj = level.overworld.objects[i]
        x = obj.x // 160
        y = obj.y // 160
        level_grid[x, y] = obj.id
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            current_obj_id = level_grid[x, y]
            if include_air or current_obj_id != -1:
                # Construct input tensor
                # 8 adjacent objects
                input_tensor = np.zeros(input_shape, dtype=np.uint8)

                # Get a nxn area (not including the center)
                # Activate neurons as applicable
                off_counter = 0
                for off_x in range(-(context_size // 2), context_size // 2 + 1):
                    for off_y in range(-(context_size // 2), context_size // 2 + 1):
                        if not (off_x == 0 and off_y == 0):
                            if not (
                                x + off_x < 0
                                or x + off_x > max_x
                                or y + off_y < 0
                                or y + off_y > max_y
                            ):
                                # Object in bounds
                                # May include empty object ID
                                obj_id = level_grid[x + off_x, y + off_y]
                                if include_air:
                                    input_tensor[
                                        (MAX_OBJECT_ID + 2) * off_counter + obj_id + 1
                                    ] = 1
                                elif obj_id != -1:
                                    input_tensor[
                                        (MAX_OBJECT_ID + 1) * off_counter + obj_id
                                    ] = 1
                            else:
                                if include_air:
                                    # Empty object ID
                                    input_tensor[
                                        (MAX_OBJECT_ID + 2) * off_counter + 0
                                    ] = 1
                            off_counter += 1

                # Works even if obj_id is -1 (nonexistant)
                output_tensor = np.zeros(output_shape, dtype=np.uint8)
                if include_air:
                    output_tensor[current_obj_id + 1] = 1
                else:
                    output_tensor[current_obj_id] = 1

                # Add tensors to choices
                if num_objects_limit != -1:
                    object_choices[current_obj_id].append((input_tensor, output_tensor))
                else:
                    input_tensors.append(input_tensor)
                    output_tensors.append(output_tensor)
                    obj_distribution[current_obj_id] += 1
    counter += 1
    if counter % 10 == 0:
        print("Processed %d" % counter)
    if counter == num_levels:
        break

# Prepare tensors
if num_objects_limit != -1:
    for id in range(-1, MAX_OBJECT_ID + 1):
        if id in object_choices:
            num_objects_limit_specific = int(
                np.log(len(object_choices[id])) * num_objects_limit
            )
            # Select n random samples
            if (
                num_objects_limit == -1
                or len(object_choices[id]) < num_objects_limit_specific
            ):
                # Less objects of this id than object limit
                for tensors in object_choices[id]:
                    input_tensors.append(tensors[0])
                    output_tensors.append(tensors[1])
                    obj_distribution[id] += 1
            else:
                # More objects of this id than object limit
                for tensors in random.sample(
                    object_choices[id], num_objects_limit_specific
                ):
                    input_tensors.append(tensors[0])
                    output_tensors.append(tensors[1])
                    obj_distribution[id] += 1
    # Clear object choices to save memory
    object_choices.clear()

# Print debugging output
print(len(input_tensors))
for num, obj_id in sorted(((v, k) for k, v in obj_distribution.items()), reverse=True):
    print("%d: %d" % (obj_id, num))

tf.random.set_seed(42)

model = tf.keras.models.Sequential(
    [
        tf.keras.Input(shape=input_shape),
        tf.keras.layers.Dense(input_shape, activation="relu"),
        tf.keras.layers.Dense(output_shape, activation="softmax"),
    ]
)

model.compile(
    optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=1e-4),
    loss=tf.keras.losses.CategoricalCrossentropy(),
    metrics=[tf.keras.metrics.CategoricalAccuracy()],
    steps_per_execution=32,
    jit_compile=True,
)
model.summary()

model.fit(
    np.array(input_tensors),
    np.array(output_tensors),
    epochs=epochs,
    batch_size=batch_size,
)
model.save(model_name)
