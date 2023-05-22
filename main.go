package main

//#cgo LDFLAGS: -L${SRCDIR} -lmarioedit
//#include "./third_party/marioedit/library/include/marioedit_library.hpp"
//#include <stdlib.h>
//#include <string.h>
import "C"
import (
	"bytes"
	"encoding/binary"
	"fmt"
	"image"
	"image/color"
	"image/gif"
	"image/png"
	"math/rand"
	"os"
	"sort"
	"time"
	"unicode/utf16"
	"unsafe"

	"github.com/mm2srv/smm2_parsing"

	"github.com/ericpauley/go-quantize/quantize"
	tf "github.com/wamuir/graft/tensorflow"
)

// Constants used for inference
// Allowed objects are declared in main as allowed_objects_slice, slices cannot be constant in Go
const MAX_OBJECT_ID = 132
const INCLUDE_AIR = false
const MODEL_NAME = "savedmodel7"
const MODEL_CONTEXT_SIZE = 7
const WIDTH = 31
const HEIGHT = 30
const ITERATIONS = 30
const AIR_PROBABILITY = 0.95
const BCD_FILENAME = ""
const RANDOM_SEED = 42

func EncodeToUCS2(str string) []byte {
	u := utf16.Encode([]rune(str))
	dst := make([]byte, len(u)*2)
	wi := 0
	for _, r := range u {
		binary.LittleEndian.PutUint16(dst[wi:], uint16(r))
		wi += 2
	}
	return dst
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

type ObjProbabilityEntry struct {
	id   int
	prob float32
}

// Set data structure (does not exist in base Go)
type set struct {
	m map[int]struct{}
}

var exists = struct{}{}

func NewSet(starting_values []int) *set {
	s := &set{}
	s.m = make(map[int]struct{})
	for _, v := range starting_values {
		s.m[v] = exists
	}
	return s
}
func (s *set) Add(value int) {
	s.m[value] = exists
}
func (s *set) Remove(value int) {
	delete(s.m, value)
}
func (s *set) Contains(value int) bool {
	_, c := s.m[value]
	return c
}

func RunInference(model *tf.SavedModel, context_list [][][]int) ([][]ObjProbabilityEntry, error) {
	input_tensor_slices := [][]float32{}
	for _, context := range context_list {
		// Prepare input slice
		context_size := len(context)
		var input_size int
		if INCLUDE_AIR {
			input_size = (MAX_OBJECT_ID + 2) * (context_size*context_size - 1)
		} else {
			input_size = (MAX_OBJECT_ID + 1) * (context_size*context_size - 1)
		}
		input_tensor_slice := make([]float32, input_size)
		off_counter := 0
		for off_x := 0; off_x < context_size; off_x++ {
			for off_y := 0; off_y < context_size; off_y++ {
				if !(off_x == context_size/2 && off_y == context_size/2) {
					obj_id := context[off_y][off_x]
					if INCLUDE_AIR {
						input_tensor_slice[(MAX_OBJECT_ID+2)*off_counter+obj_id+1] = 1
					} else if obj_id != -1 {
						input_tensor_slice[(MAX_OBJECT_ID+1)*off_counter+obj_id] = 1
					}
					off_counter++
				}
			}
		}
		input_tensor_slices = append(input_tensor_slices, input_tensor_slice)
	}

	// Create input tensor
	input_tensor, err := tf.NewTensor(input_tensor_slices)
	if err != nil {
		return [][]ObjProbabilityEntry{}, err
	}

	// Run inference
	result, err := model.Session.Run(
		map[tf.Output]*tf.Tensor{
			model.Graph.Operation("serving_default_input_1").Output(0): input_tensor,
		},
		[]tf.Output{
			model.Graph.Operation("StatefulPartitionedCall").Output(0),
		},
		nil,
	)
	if err != nil {
		return [][]ObjProbabilityEntry{}, err
	}

	output_entries_list := [][]ObjProbabilityEntry{}
	for _, result := range result[0].Value().([][]float32) {
		// Get most likely block (or no block at all (-1))
		var output_entries []ObjProbabilityEntry
		for i, prob := range result {
			if INCLUDE_AIR {
				output_entries = append(output_entries, ObjProbabilityEntry{
					id:   i - 1,
					prob: prob,
				})
			} else {
				output_entries = append(output_entries, ObjProbabilityEntry{
					id:   i,
					prob: prob,
				})
			}
		}
		sort.Slice(output_entries, func(i, j int) bool {
			return output_entries[i].prob > output_entries[j].prob
		})
		output_entries_list = append(output_entries_list, output_entries)
	}

	return output_entries_list, nil
}

func RunInferenceAlt(model *tf.SavedModel, obj1_id int, obj2_id int, obj3_id int, obj4_id int, obj5_id int, obj6_id int, obj7_id int, obj8_id int) ([]ObjProbabilityEntry, error) {
	// Prepare input slice
	var input_tensor_slice [8]float32
	input_tensor_slice[0] = float32(obj1_id + 1)
	input_tensor_slice[1] = float32(obj2_id + 1)
	input_tensor_slice[2] = float32(obj3_id + 1)
	input_tensor_slice[3] = float32(obj4_id + 1)
	input_tensor_slice[4] = float32(obj5_id + 1)
	input_tensor_slice[5] = float32(obj6_id + 1)
	input_tensor_slice[6] = float32(obj7_id + 1)
	input_tensor_slice[7] = float32(obj8_id + 1)

	// Create input tensor
	input_tensor, err := tf.NewTensor([][8]float32{input_tensor_slice})
	if err != nil {
		return []ObjProbabilityEntry{}, err
	}

	// Run inference
	result, err := model.Session.Run(
		map[tf.Output]*tf.Tensor{
			model.Graph.Operation("serving_default_input_1").Output(0): input_tensor,
		},
		[]tf.Output{
			model.Graph.Operation("StatefulPartitionedCall").Output(0),
		},
		nil,
	)
	if err != nil {
		return []ObjProbabilityEntry{}, err
	}

	// Get most likely block
	output := result[0].Value().([][]float32)[0]
	var output_entries []ObjProbabilityEntry
	for i, prob := range output {
		output_entries = append(output_entries, ObjProbabilityEntry{
			id:   i,
			prob: prob,
		})
	}
	sort.Slice(output_entries, func(i, j int) bool {
		return output_entries[i].prob > output_entries[j].prob
	})
	return output_entries, nil
}

func GenerateImage(bcd *smm2_parsing.BCD, width int, height int) ([]byte, error) {
	level_data, _ := bcd.SaveDecrypted()
	level_data_pointer := (*C.uchar)(unsafe.Pointer(&level_data[0]))

	asset_folder := C.CString("./third_party/marioedit/marioedit")
	defer C.free(unsafe.Pointer(asset_folder))

	var thumbnail_size C.int
	// uint8_t* MarioEdit_GetJpeg(uint8_t* level_data, size_t level_size, char* asset_folder, int width, int height, int offset_x, int offset_y, int* thumbnail_size);
	thumbnail := C.MarioEdit_GetFullPng(level_data_pointer, C.ulong(len(level_data)), asset_folder, C.int(width*16), C.int(height*16), 0, 0, (*C.int)(unsafe.Pointer(&thumbnail_size)))
	defer C.MarioEdit_FreeImage(thumbnail)

	return C.GoBytes(unsafe.Pointer(thumbnail), thumbnail_size), nil
}

func RunDiffusion(model *tf.SavedModel, width int, height int, start_x int, start_y int, end_x int, end_y int, iterations int, air_prob float64, r *rand.Rand, grid [][]int, allowed_objects *set, context_size int) ([][]int, error) {
	// Initialize bounds
	if start_x == -1 {
		start_x = 0
	}
	if start_y == -1 {
		start_y = 0
	}
	// Ends are exclusive
	if end_x == -1 {
		end_x = width
	}
	if end_y == -1 {
		end_y = height
	}

	// Run diffusion iterations
	for i := 0; i < iterations; i++ {
		now := time.Now()

		// Create new grid to apply changes to
		// Use copy of previous grid
		new_grid := make([][]int, height)
		for y := 0; y < height; y++ {
			new_grid[y] = make([]int, width)
			copy(new_grid[y], grid[y])
		}

		for y := start_y; y < end_y; y++ {
			context_list := [][][]int{}
			for x := start_x; x < end_x; x++ {
				// Start with no defined objects in context
				context := make([][]int, context_size)
				for i := 0; i < context_size; i++ {
					context[i] = make([]int, context_size)
					for j := 0; j < context_size; j++ {
						context[i][j] = -1
					}
				}

				// Get defined context
				for y_context := max(y-context_size/2, 0); y_context < min(y+context_size/2+1, height); y_context++ {
					for x_context := max(x-context_size/2, 0); x_context < min(x+context_size/2+1, width); x_context++ {
						context[y-y_context+context_size/2][x-x_context+context_size/2] = grid[y_context][x_context]
					}
				}

				// Add to list of contexes
				context_list = append(context_list, context)
			}

			// Run inference on all contexes
			results, err := RunInference(model, context_list)
			if err != nil {
				return [][]int{}, err
			}

			for x := 0; x < (end_x - start_x); x++ {
				// If the first result has a lower probability than the air use air instead
				if float64(results[x][0].prob) < air_prob {
					new_grid[y][x+start_x] = -1
					continue
				}

				// Choose first object in allowed objects
				for i := 0; i < len(results); i++ {
					if allowed_objects.Contains(results[x][i].id) {
						new_grid[y][x+start_x] = results[x][i].id
						break
					}
				}
			}
		}

		// Apply grid changes
		grid = new_grid

		fmt.Println("Iteration took", time.Since(now))
	}

	return grid, nil
}

func RunDiffusionWithGif(model *tf.SavedModel, width int, height int, start_x int, start_y int, end_x int, end_y int, iterations int, air_prob float64, r *rand.Rand, grid [][]int, allowed_objects *set, context_size int, bcd *smm2_parsing.BCD) error {
	gif_images := []image.Image{}

	for i := 0; i < iterations+1; i++ {
		if i != 0 {
			var err error
			grid, err = RunDiffusion(model, width, height, start_x, start_y, end_x, end_y, 1, air_prob, r, grid, allowed_objects, context_size)
			if err != nil {
				return err
			}
		}

		PackObjectGrid(grid, bcd, width, height)

		image_bytes, err := GenerateImage(bcd, width, height)
		if err != nil {
			return err
		}

		img, err := png.Decode(bytes.NewReader(image_bytes))
		if err != nil {
			return err
		}
		gif_images = append(gif_images, img)
	}

	// Open image file
	filename := fmt.Sprintf("test-%d.gif", rand.Uint64())
	gif_f, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		return err
	}
	defer gif_f.Close()

	gif_out := &gif.GIF{}
	for i, img := range gif_images {
		// Quantize image
		bounds := img.Bounds()
		quantizer := quantize.MedianCutQuantizer{}
		palette := quantizer.Quantize(make([]color.Color, 0, 256), img)
		paletted := image.NewPaletted(bounds, palette)

		// Set pixels manually
		for y := bounds.Min.Y; y < bounds.Max.Y; y++ {
			for x := bounds.Min.X; x < bounds.Max.X; x++ {
				paletted.Set(x, y, palette.Convert(img.At(x, y)))
			}
		}

		// Add new frame to animated GIF
		gif_out.Image = append(gif_out.Image, paletted)
		if i == len(gif_images)-1 {
			gif_out.Delay = append(gif_out.Delay, 300)
		} else {
			gif_out.Delay = append(gif_out.Delay, 5)
		}
	}

	// Encode GIF
	gif.EncodeAll(gif_f, gif_out)
	fmt.Println(filename)

	return nil
}

func PackObjectGrid(object_grid [][]int, bcd *smm2_parsing.BCD, width int, height int) {
	// Add objects
	object_index := 0
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			if object_grid[y][x] != -1 {
				bcd.OverWorld.Objects[object_index] = smm2_parsing.Object{
					X:      uint32(x*160 + 80),
					Y:      uint32(y*160 + 80),
					Width:  1,
					Height: 1,
					Flag:   100663360,
					CFlag:  100663360,
					CId:    0xFFFF,
					LId:    0xFFFF,
					SId:    0xFFFF,
					Id:     uint16(object_grid[y][x]),
				}
				object_index++
			}
		}
	}
	bcd.OverWorld.ObjectCount = uint32(object_index + 1)
}

func main() {
	bcd := &smm2_parsing.BCD{}

	// width * height must not exceed 3000, an exception will be thrown otherwise
	bcd.Header.YStart = 3
	bcd.Header.XGoal = uint16((WIDTH-10)*10 + 5)
	bcd.Header.YGoal = 3
	bcd.Header.TimeLimit = 100
	copy(bcd.Header.GameStyle[:], "M1")
	copy(bcd.Header.Name[:], EncodeToUCS2("Awesome Test Course"))
	copy(bcd.Header.Description[:], EncodeToUCS2("Play this awesome course!"))

	// TODO put enums in smm2_parsing
	bcd.OverWorld.Theme = 2
	bcd.OverWorld.Orientation = 0
	bcd.OverWorld.BoundaryRight = uint32(WIDTH * 16)
	bcd.OverWorld.BoundaryTop = uint32(HEIGHT * 16)

	bcd.OverWorld.GroundCount = 0

	// Specify allowed objects
	allowed_objects_slice := []int{4, 5, 6, 8}
	//allowed_objects_slice := []int{0, 1, 4, 19, 63, 64}
	allowed_objects := NewSet(allowed_objects_slice)
	r := rand.New(rand.NewSource(RANDOM_SEED))

	// Initialize grid
	object_grid := make([][]int, HEIGHT)
	for y := 0; y < HEIGHT; y++ {
		object_grid[y] = make([]int, WIDTH)
		for x := 0; x < WIDTH; x++ {
			object_grid[y][x] = -1
		}
	}

	// Generate noise
	for x := 5; x < WIDTH; x++ {
		for y := 3; y < HEIGHT; y++ {
			object_grid[y][x] = allowed_objects_slice[r.Intn(len(allowed_objects_slice))]
		}
	}

	// Suppress tensorflow logging to errors only
	os.Setenv("TF_CPP_MIN_LOG_LEVEL", "3")

	// Load model from disk
	model, err := tf.LoadSavedModel(MODEL_NAME, []string{"serve"}, nil)
	if err != nil {
		panic(err)
	}
	defer model.Session.Close()

	// Run diffusion
	err = RunDiffusionWithGif(model, WIDTH, HEIGHT, 5, 3, -1, -1, ITERATIONS, AIR_PROBABILITY, r, object_grid, allowed_objects, MODEL_CONTEXT_SIZE, bcd)
	if err != nil {
		panic(err)
	}

	// Generate BCD file if specified
	if len(BCD_FILENAME) != 0 {
		level_bytes, err := bcd.Save()
		if err != nil {
			panic(err)
		}

		err = os.WriteFile(BCD_FILENAME, level_bytes, 0644)
		if err != nil {
			panic(err)
		}
	}
}
