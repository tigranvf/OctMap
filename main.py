from time import perf_counter as pc
from random import randrange
from settings import *
from pygame.locals import *
from modules import *
import pygame
import json

try:
    open("map.json", "r").close()
except FileNotFoundError:
    import parser

print("Loading google maps")

with open("map.json", "r") as file:
    json_oct_map = json.load(file)

oct_map = [[Tile() for y in range(tile_height)] for x in range(tile_width)]

for x, col in enumerate(json_oct_map):
    for y, el in enumerate(col):
        if type(el) == str:
            oct_map[x][y].type = el
        else:
            oct_map[x][y].color = el

print("Intializing screen")

screen = pygame.display.set_mode(res)

last_tick = pc()


def render(cell: Cell):
    vertexes = []
    for i in range(6):
        vertexes.append(((cell.pos.x if cell.pos.y % 2 else cell.pos.x + 0.5) * horiz + cos(60 * i - 30) * tile,
                         cell.pos.y * vert + sin(60 * i - 30) * tile))
    # for vertex in vertexes:
    #     pygame.draw.circle(screen, (255, 255, 255), vertex, 1)
    pygame.draw.polygon(screen, cell.color, vertexes)
    if outline:
        pygame.draw.polygon(screen, black, vertexes, 1)


cells = [[Cell(x, y, oct_map[x][y].cell_color) for y in range(tile_height)] for x in range(tile_width)]

print("Init was ended")
rendered = False
# main loop
while True:
    # check if we want to close the window
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # calculating delta time from last tick (can be used in future)
    #deltaTime = pc() - last_tick
    #last_tick = pc()

    # clear the screen
    #screen.fill(black)

    # render cells
    if not rendered:
        for col in cells:
            for cell in col:
                render(cell)
        rendered = True

    # update the screen
    pygame.display.flip()