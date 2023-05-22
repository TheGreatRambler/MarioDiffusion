from datasets import load_dataset
import zlib
from io import BytesIO
from level import Level
from kaitaistruct import KaitaiStream
import numpy as np
import tensorflow as tf
from tqdm.keras import TqdmCallback

ds = load_dataset("TheGreatRambler/mm2_level", streaming=True, split="train")

MAX_OBJECT_ID = 132
input_tensors = []
output_tensors = []
context_size = 5  # 3x3 context size
input_shape = context_size * context_size - 1
output_shape = MAX_OBJECT_ID + 1

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
    for x in range(context_size - 2, max_x - context_size + 3):
        for y in range(context_size - 2, max_y - context_size + 3):
            if level_grid[x, y] != -1:
                # Construct input tensor
                input_tensor = np.zeros(input_shape, dtype=np.uint8)

                # Get a nxn area (not including the center)
                off_counter = 0
                for off_x in range(-(context_size // 2), context_size // 2 + 1):
                    for off_y in range(-(context_size // 2), context_size // 2 + 1):
                        if not (off_x == 0 and off_y == 0):
                            obj_id = level_grid[x + off_x, y + off_y]
                            # Includes no object
                            input_tensor[off_counter] = obj_id + 1
                            off_counter += 1

                current_obj_id = level_grid[x, y]
                output_tensor = np.zeros(output_shape, dtype=np.uint8)
                output_tensor[current_obj_id] = 1

                input_tensors.append(input_tensor)
                output_tensors.append(output_tensor)
    counter += 1
    if counter % 10 == 0:
        print("Processed %d" % counter)
    if counter == 1000:
        break

tf.random.set_seed(42)

model = tf.keras.models.Sequential(
    [
        tf.keras.Input(shape=input_shape),
        tf.keras.layers.Dense(input_shape, activation="relu"),
        tf.keras.layers.Dense(output_shape * 2, activation="relu"),
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
    epochs=75,
    batch_size=128,
)
model.save("../savedmodelalt")
