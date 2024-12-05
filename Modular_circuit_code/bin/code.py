import board
import neopixel
import random
import time

# Configure the pin connected to the NeoPixel data line
pixel_pin = board.GP28  # Change this to the GPIO pin you're using

# Total LEDs (excluding skipped ones)
num_leds = 300
leds_per_row = 24  # LEDs per row in your grid
num_rows = num_leds // leds_per_row  # Calculate the number of rows

# NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_leds, brightness=0.5, auto_write=False)
COLORS = {
    "RED": (0, 255, 0),
    "GREEN": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "YELLOW": (255, 255, 0),
    "ORANGE": (255, 128, 0),
    "PURPLE": (128, 0, 255),
    "LIME": (128, 255, 0),
    "TEAL": (0, 255, 128),
    "PASTEL_GREEN": (192, 64, 64),
    "PASTEL_BLUE": (64, 64, 255),
    "PASTEL_RED": (64, 255, 64),
    "PASTEL_PURPLE": (128, 64, 192),
    "PASTEL_YELLOW": (192, 192, 64),
    "SKY_BLUE": (64, 128, 255),
    "SUNSET": (255, 64, 32),
    "AQUA": (64, 255, 192),
    "MAGENTA": (255, 0, 128),
    "GOLD": (255, 192, 0),
    "TURQUOISE": (64, 255, 128),
    "PEACH": (255, 64, 64),
    "INDIGO": (64, 0, 255),
    "CHARTREUSE": (128, 255, 0),
    "OLIVE": (128, 128, 0),
    "GRAY": (128, 128, 128),
    "DARK_GRAY": (64, 64, 64),
    "LIGHT_GRAY": (192, 192, 192),
    "MINT": (128, 255, 192),
    "LAVENDER": (192, 128, 255),
    "ROSE": (255, 128, 192),
    "CORAL": (255, 128, 64),
    "CYAN": (0, 255, 255),
    "PINK": (255, 0, 255),
    "OFF": (0, 0, 0),
}

def get_random_color():
    """Returns a random color tuple from the COLORS dictionary."""
    return random.choice(list(COLORS.values()))# Define your LED coordinate mapping
ids_by_coord = [
    [297, 298, 287, 286, 279, 278, 270, 269, 262, 261, 254, 253, 245, 244, 237, 236, 229, 228, 220, 219, 212, 211, 204, 203],
    [296, 295, 288, 285, 280, 277, 271, 268, 263, 260, 255, 252, 246, 243, 238, 235, 230, 227, 221, 218, 213, 210, 205, 202],
    [293, 294, 289, 284, 281, 276, 272, 267, 264, 259, 256, 251, 247, 242, 239, 234, 231, 226, 222, 217, 214, 209, 206, 201],
    [292, 291, 290, 283, 282, 275, 273, 266, 265, 258, 257, 250, 248, 241, 240, 233, 232, 225, 223, 216, 215, 208, 207, 200],
    [106, 107, 108, 115, 116, 123, 125, 132, 133, 140, 141, 148, 150, 157, 158, 165, 166, 173, 175, 182, 183, 190, 191, 198],
    [105, 104, 109, 114, 117, 122, 126, 131, 134, 139, 142, 147, 151, 156, 159, 164, 167, 172, 176, 181, 184, 189, 192, 197],
    [102, 103, 110, 113, 118, 121, 127, 130, 135, 138, 143, 146, 152, 155, 160, 163, 168, 171, 177, 180, 185, 188, 193, 196],
    [101, 100, 111, 112, 119, 120, 128, 129, 136, 137, 144, 145, 153, 154, 161, 162, 169, 170, 178, 179, 186, 187, 194, 195],
    [97, 98, 87, 86, 79, 78, 70, 69, 62, 61, 54, 53, 45, 44, 37, 36, 29, 28, 20, 19, 12, 11, 4, 3],
    [96, 95, 88, 85, 80, 77, 71, 68, 63, 60, 55, 52, 46, 43, 38, 35, 30, 27, 21, 18, 13, 10, 5, 2],
    [93, 94, 89, 84, 81, 76, 72, 67, 64, 59, 56, 51, 47, 42, 39, 34, 31, 26, 22, 17, 14, 9, 6, 1],
    [92, 91, 90, 83, 82, 75, 73, 66, 65, 58, 57, 50, 48, 41, 40, 33, 32, 25, 23, 16, 15, 8, 7, 0]
]

# Map coordinates to the LED ID
def coords_to_id(x, y):
    try:
        return ids_by_coord[y][x]
    except IndexError:
        return None

# Map LED ID to coordinates
def id_to_coords(led_id):
    for y, row in enumerate(ids_by_coord):
        for x, id in enumerate(row):
            if id == led_id:
                return (x, y)
    return None

def light_up_grid_horizontal(start, delay, color):
    if start.lower() in ['top', 't', '1']:
        for y in range(len(ids_by_coord)):
            for x in range(len(ids_by_coord[y])):
                index = coords_to_id(x, y)
                pixels[index] = color 
            pixels.show()
            time.sleep(delay)
    elif start.lower() in ['bottom', 'b', '0']:
        for y in range(len(ids_by_coord) - 1, -1, -1):
            for x in range(len(ids_by_coord[y])):
                index = coords_to_id(x, y)
                pixels[index] = color
            pixels.show()
            time.sleep(delay)

def light_up_grid_vertical(start, delay, color):
    if start.lower() in ['left', 'l', '1']:
        for x in range(len(ids_by_coord[0]) - 1, -1, -1):
            for y in range(len(ids_by_coord)):
                index = coords_to_id(x, y)
                pixels[index] = color 
            pixels.show()
            time.sleep(delay)
    elif start.lower() in ['right', 'r', '0']:
        for x in range(len(ids_by_coord[0])):
            for y in range(len(ids_by_coord)):
                index = coords_to_id(x, len(ids_by_coord) - 1 - y)
                pixels[index] = color
            pixels.show()
            time.sleep(delay)

def light_up_grid(direction, start, delay, color):
    if direction.lower() in ['horizontal','h','1']:
        light_up_grid_horizontal(start, delay, color)
    if direction.lower() in ['vertical', 'v','0']:
        light_up_grid_vertical(start, delay, color)

# Function to create pixel representation of the text
def create_pixel_representation(text):
    char_map = {
        'A': [
            [0, 1, 0],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'B': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
        ],
        'C': [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [0, 1, 1],
        ],
        'D': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 0],
        ],
        'E': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 0],
            [1, 0, 0],
            [1, 1, 1],
        ],
        'F': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 0],
            [1, 0, 0],
            [1, 0, 0],
        ],
        'G': [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 1],
        ],
        'H': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'I': [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1],
        ],
        'J': [
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
        ],
        'K': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'L': [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1],
        ],
        'M': [
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'N': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'O': [
            [0, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
        ],
        'P': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 0],
            [1, 0, 0],
        ],
        'Q': [
            [0, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 1],
        ],
        'R': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'S': [
            [0, 1, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 0],
        ],
        'T': [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
        'U': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
        ],
        'V': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
        ],
        'W': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 0],
        ],
        'X': [
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
        ],
        'Y': [
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
        'Z': [
            [1, 1, 1],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1],
        ],
        ' ': [ 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
    }
    representation = []
    for char in text:
        if char in char_map:
            representation.extend(char_map[char])
            representation.append([0] * 3) 

    return representation


# turn off all 
def clear_grid():
    for i in range(num_leds):
        pixels[i] = OFF
    pixels.show()

# color border
def borders(rows, cols):
    for i in range(num_leds):
        if ((i + 1) % 25 == 0):
            continue
        elif coords_by_id[i][0] == 0 or coords_by_id[i][0] == 23:
            pixels[i] = Colors["GREEN"]
        elif coords_by_id[i][1] == 0 or coords_by_id[i][1] == 11:
            pixels[i] = Colors["GREEN"]
        else:
            pixels[i] = Colors["WHITE"]
    pixels.show()
    time.sleep(0.5)

# color by coordinates
def color_coords(x, y):
    index = coords_to_id(x, y)
    if index is not None:
        pixels[index - 1] = Colors["RED"]
        pixels.show()
    time.sleep(0.5)

# color by led id
def color_id(id):
    pixels[id] = Colors["GREEN"]
    pixels.show()

def draw_from_grid(drawing, color1, color2):
    for y in range(12):
        for x in range(24):
            index = coords_to_id(x, y)
            if drawing[y][x] == 1:
                pixels[index ] = color1
            else:
                pixels[index] = color2
    pixels.show()
    time.sleep(0.5)

# not working well
def move_right():
    for y in range(12):
        for x in range(24):
            index_left = coords_to_id(x, y)
            index = coords_to_id(x, y)
            if pixels[index_left] == Colors["GREEN"]:
                pixels[index] = Colors["GREEN"]
                pixels[index_left] = Colors["OFF"]
        pixels.show()
    time.sleep(0.5)

# Main loop for experimenting
while True:
    delay_in_seconds = 60 / (4000)
    position = random.choice(['1', '0'])
    direction = random.choice(['1', '0'])
    light_up_grid(direction, position, delay_in_seconds, get_random_color())
    position = random.choice(['1', '0'])
    direction = random.choice(['1', '0'])
    light_up_grid(direction, position, delay_in_seconds, get_random_color())