from modules import *

api_key = ""  # api key from google maps
map_x, map_y = 47.65, -122.35  # coordinates on google map
map_zoom = 12  # zoom
map_width, map_height = 480, 360  # size of parsing image
map_size = f"{map_width}x{map_height}"

min_num_road = 10  # minimum number of pixels that contain road in one tile.

tile = 8  # size of tile
horiz, vert = sqrt(3) * tile, 3/2 * tile
res = width, height = horiz*40, vert*30  # resolution of window
tile_width, tile_height = int(width//horiz)+2, int(height//vert)+1

if tile_width < width/horiz:
    tile_width += 1
if tile_height < height/vert:
    tile_height += 1

tile_map_width, tile_map_height = int(map_width//tile_width), int(map_height//tile_height)
print(tile_map_width, tile_map_height)

img_path = "staticmap.png"
black = (0, 0, 0)
white = (255, 255, 255)
