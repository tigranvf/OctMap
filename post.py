from settings import *
import copy


def main(oct_map):
    print("Post processing...")
    new_oct_map = [[Tile() for y in range(tile_height)] for x in range(tile_width)]

    for x, col in enumerate(oct_map):
        for y, el in enumerate(col):
            if el.type == "road":
                mod = y % 2
                roads = 0
                broken = True

                if 0 <= x - mod < tile_width and 0 <= y - 1 < tile_height:
                    tile1 = oct_map[x - mod][y - 1]
                else:
                    tile1 = None

                if 0 <= x - mod + 1 < tile_width and 0 <= y - 1 < tile_height:
                    tile2 = oct_map[x - mod + 1][y - 1]
                else:
                    tile2 = None

                if 0 <= x - 1 < tile_width and 0 <= y < tile_height:
                    tile3 = oct_map[x - 1][y]
                else:
                    tile3 = None

                if 0 <= x + 1 < tile_width and 0 <= y < tile_height:
                    tile4 = oct_map[x + 1][y]
                else:
                    tile4 = None

                if 0 <= x - mod < tile_width and 0 <= y + 1 < tile_height:
                    tile5 = oct_map[x - mod][y + 1]
                else:
                    tile5 = None

                if 0 <= x - mod + 1 < tile_width and 0 <= y + 1 < tile_height:
                    tile6 = oct_map[x - mod + 1][y + 1]
                else:
                    tile6 = None

                if tile1 and tile2:
                    if tile1.type == tile2.type == "road":
                        broken = False
                if tile2 and tile4:
                    if tile2.type == tile4.type == "road":
                        broken = False
                if tile4 and tile6:
                    if tile4.type == tile6.type == "road":
                        broken = False
                if tile6 and tile5:
                    if tile6.type == tile5.type == "road":
                        broken = False
                if tile5 and tile3:
                    if tile5.type == tile3.type == "road":
                        broken = False
                if tile3 and tile1:
                    if tile3.type == tile1.type == "road":
                        broken = False

                if tile1 and tile6:
                    if tile1.type == tile6.type == "road":
                        temp = [True, True]

                        if tile2:
                            if tile2.type == "road":
                                temp[0] = False
                        if tile3:
                            if tile3.type == "road":
                                temp[0] = False

                        if tile4:
                            if tile4.type == "road":
                                temp[1] = False
                        if tile5:
                            if tile5.type == "road":
                                temp[1] = False
                        if temp[0] or temp[1]:
                            broken = True
                if tile2 and tile5:
                    if tile2.type == tile5.type == "road":
                        temp = [True, True]

                        if tile1:
                            if tile1.type == "road":
                                temp[0] = False
                        if tile4:
                            if tile4.type == "road":
                                temp[0] = False

                        if tile3:
                            if tile3.type == "road":
                                temp[1] = False
                        if tile6:
                            if tile6.type == "road":
                                temp[1] = False

                        if temp[0] or temp[1]:
                            broken = True
                if tile3 and tile4:
                    if tile3.type == tile4.type == "road":
                        temp = [True, True]

                        if tile1:
                            if tile1.type == "road":
                                temp[0] = False
                        if tile5:
                            if tile5.type == "road":
                                temp[0] = False

                        if tile2:
                            if tile2.type == "road":
                                temp[1] = False
                        if tile6:
                            if tile6.type == "road":
                                temp[1] = False

                        if temp[0] or temp[1]:
                            broken = True

                if not broken:
                    count = {"city": 0, "forest": 0, "water": 0}

                    if tile1:
                        try:
                            count[tile1.type] += 1
                        except KeyError:
                            ...
                    if tile2:
                        try:
                            count[tile2.type] += 1
                        except KeyError:
                            ...
                    if tile3:
                        try:
                            count[tile3.type] += 1
                        except KeyError:
                            ...
                    if tile4:
                        try:
                            count[tile4.type] += 1
                        except KeyError:
                            ...
                    if tile5:
                        try:
                            count[tile5.type] += 1
                        except KeyError:
                            ...
                    if tile6:
                        try:
                            count[tile6.type] += 1
                        except KeyError:
                            ...

                    if count["forest"] < count["city"] > count["water"]:
                        oct_map[x][y].type = "city"
                    if count["city"] < count["forest"] > count["water"]:
                        oct_map[x][y].type = "forest"
                    if count["forest"] < count["water"] > count["city"]:
                        oct_map[x][y].type = "water"

                else:
                    oct_map[x][y].type = "road"
            else:
                oct_map[x][y].type = el.type

    return oct_map