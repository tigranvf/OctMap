from modules import *

api_key = ""  # api key from google maps
map_x, map_y = 47.65, -122.35  # coordinates on google map
map_zoom = 12  # zoom
map_width, map_height = 480, 360  # size of parsing image
map_size = f"{map_width}x{map_height}"

num_of_posts = 5
types = [
    "water",
    "forest",
    "city",
    "road"
]

post_processing = True

min_num_road = 0  # minimum number of pixels that contain road in one tile.

end_of_map_tile = "undefined"

priority = {
    "city": 0,
    "forest": 0.1,
    "water": 0.2
}

tile = 8  # size of tile
outline = True
horiz, vert = sqrt(3) * tile, 3/2 * tile
res = width, height = horiz*120, vert*90  # resolution of window
tile_width, tile_height = int(width//horiz), int(height//vert)

if tile_width < width/horiz:
    tile_width += 1
if tile_height < height/vert:
    tile_height += 1

tile_map_width, tile_map_height = int(map_width//tile_width), int(map_height//tile_height)
print(tile_map_width, tile_map_height)

img_path = "staticmap.png"
black = (0, 0, 0)
white = (255, 255, 255)
