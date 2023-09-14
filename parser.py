from copy import deepcopy
from settings import *
from PIL import Image
from modules import *
import requests
import post
import json

print("Getting google maps")

# parsing google map image
with open(img_path, "wb") as file:
    file.write(requests.get(
        f"https://maps.googleapis.com/maps/api/staticmap?key={api_key}&center={map_x},{map_y}&zoom={map_zoom}&format=png&maptype=roadmap&style=element:labels|visibility:off&style=feature:administrative.land_parcel|visibility:off&style=feature:administrative.neighborhood|visibility:off&size={map_size}").content)

print("Loading google maps")

img = Image.open(img_path)
img.load()
img = img.convert("RGB")

oct_map = [[Tile() for y in range(tile_height)] for x in range(tile_width)]

print("Filtering google maps")

# convert image to oct map
for x in range(tile_width):
    for y in range(tile_height):
        # check for roads (we can add another types of units)
        road = 0
        pre_avg_color = [0, 0, 0, 0]
        for px in range(tile_map_width):
            for py in range(tile_map_height):
                pixel = img.getpixel((x * tile_map_width + px, y * tile_map_height + py))
                for n, col in enumerate(pixel):
                    pre_avg_color[n] += col
                pre_avg_color[3] += 1
                if pixel[0] > 240 > pixel[1] and pixel[2] < 200:
                    road += 1
        if road > min_num_road:
            oct_map[x][y].type = "road"
        # if no road in cell color will be from map
        else:
            avg_color = [int(col // pre_avg_color[3])
                         for col in pre_avg_color[:-1]]
            if avg_color[0] < avg_color[1] > avg_color[2]:
                oct_map[x][y].type = "forest"
            elif avg_color[0] + 10 < avg_color[2] > avg_color[1] + 10:
                oct_map[x][y].type = "water"
            else:
                oct_map[x][y].type = "city"

if post_processing:
    old_oct_map = deepcopy(oct_map)
    oct_map = post.main(oct_map)

    while old_oct_map != oct_map:
        old_oct_map = deepcopy(oct_map)
        oct_map = post.main(oct_map)


def save():
    json_oct_map = [[None for y in range(tile_height)] for x in range(tile_width)]

    for x, col in enumerate(oct_map):
        for y, el in enumerate(col):
            json_oct_map[x][y] = el.type

    print("Saving google maps")

    with open("map.json", "w") as file:
        json.dump(json_oct_map, file)


save()
