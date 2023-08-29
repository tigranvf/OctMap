from time import perf_counter as pc
from random import randrange

import requests

from settings import *
from pygame.locals import *
from PIL import Image
from modules import *
import pygame

screen = pygame.display.set_mode(res)

# parsing google map image
with open(img_path, "wb") as file:
    file.write(requests.get(f"https://maps.googleapis.com/maps/api/staticmap?key={api_key}&center={map_x},{map_y}&zoom={map_zoom}&format=png&maptype=roadmap&style=element:labels|visibility:off&style=feature:administrative.land_parcel|visibility:off&style=feature:administrative.neighborhood|visibility:off&size={map_size}").content)


# oct cell
class Cell:
    def __init__(self, x, y, color):
        self.pos = Vector(x, y)
        self.color = color

    def render(self):
        vertexes = []
        for i in range(6):
            vertexes.append(((self.pos.x if self.pos.y % 2 else self.pos.x+0.5)*horiz+cos(60*i-30)*tile, self.pos.y*vert+sin(60*i-30)*tile))
        # for vertex in vertexes:
        #     pygame.draw.circle(screen, (255, 255, 255), vertex, 1)
        pygame.draw.polygon(screen, self.color, vertexes)


last_tick = pc()

img = Image.open(img_path)
img.load()
img = img.convert("RGB")

cells = []

# convert image to oct map
for x in range(tile_width):
    for y in range(tile_height):
        # check for roads (we can add another types of units)
        road = False
        for px in range(tile_map_width):
            for py in range(tile_map_height):
                pixel = img.getpixel((x*tile_map_width+px, y*tile_map_height+py))
                if pixel[0] > 240 > pixel[1] and pixel[2] < 200:
                    road = True
        if road:
            cells.append(Cell(x, y, (250, 200, 0)))
        # if no road in cell color will be from map
        else:
            cells.append(Cell(x, y, img.getpixel((x*tile_map_width, y*tile_map_height))))

# main loop
while True:
    # check if we want to close the window
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # calculating delta time from last tick (can be used in future)
    deltaTime = pc() - last_tick
    last_tick = pc()

    # clear the screen
    screen.fill(black)

    # render cells
    for cell in cells:
        cell.render()

    # update the screen
    pygame.display.flip()