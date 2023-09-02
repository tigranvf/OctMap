from settings import *
import copy


def get_neighborhoods(oct_map, x, y):
    mod = y % 2

    if 0 <= x - mod < tile_width and 0 <= y - 1 < tile_height:
        tile1 = oct_map[x - mod][y - 1]
    else:
        tile1 = Tile()
        tile1.type = end_of_map_tile
    if 0 <= x - mod + 1 < tile_width and 0 <= y - 1 < tile_height:
        tile2 = oct_map[x - mod + 1][y - 1]
    else:
        tile2 = Tile()
        tile2.type = end_of_map_tile
    if 0 <= x - 1 < tile_width and 0 <= y < tile_height:
        tile3 = oct_map[x - 1][y]
    else:
        tile3 = Tile()
        tile3.type = end_of_map_tile
    if 0 <= x + 1 < tile_width and 0 <= y < tile_height:
        tile4 = oct_map[x + 1][y]
    else:
        tile4 = Tile()
        tile4.type = end_of_map_tile
    if 0 <= x - mod < tile_width and 0 <= y + 1 < tile_height:
        tile5 = oct_map[x - mod][y + 1]
    else:
        tile5 = Tile()
        tile5.type = end_of_map_tile
    if 0 <= x - mod + 1 < tile_width and 0 <= y + 1 < tile_height:
        tile6 = oct_map[x - mod + 1][y + 1]
    else:
        tile6 = Tile()
        tile6.type = end_of_map_tile

    return tile1, tile2, tile4, tile6, tile5, tile3


def first_check(tiles):
    stay = True

    for i in range(6):
        if tiles[i].type == tiles[(i + 1) % 6].type == "road":
            stay = False

    return stay


def second_check(tiles, stay: bool, i) -> bool:
    a, b = i, i + 3

    if tiles[a].type == tiles[b].type == "road":
        temp = [True, True]

        if tiles[a - 1].type == "road":
            temp[0] = False
        if tiles[a + 1].type == "road":
            temp[0] = False
        if tiles[b - 1].type == "road":
            temp[1] = False
        if tiles[(b + 1) % 6].type == "road":
            temp[1] = False

        if temp[0] or temp[1]:
            return True

    return stay


def main(oct_map):
    print("Post processing...")

    # new_oct_map = [[Tile() for y in range(tile_height)] for x in range(tile_width)]

    for x, col in enumerate(oct_map):
        for y, el in enumerate(col):
            if el.type == "road":
                tiles = get_neighborhoods(oct_map, x, y)

                stay = first_check(tiles)

                for i in range(3):
                    stay = second_check(tiles, stay, i)

                if not stay:
                    count = {"city": 0, "forest": 0, "water": 0}

                    for i in range(6):
                        try:
                            count[tiles[i].type] += 1
                        except KeyError:
                            ...

                    count = sorted(count, key=lambda key: count[key] + priority[key], reverse=True)

                    oct_map[x][y].type = count[0]

                else:
                    oct_map[x][y].type = "road"
            else:
                oct_map[x][y].type = el.type

    return oct_map
