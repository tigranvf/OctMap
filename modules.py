import pygame
import math

render_road_color = (240, 200, 0)
render_forest_color = (100, 230, 100)
render_water_color = (100, 100, 230)
render_city_color = (230, 230, 230)

class Vector:
    def __init__(self, x: int, y = None):
        self.x, self.y = x, y

    def __repr__(self):
        return str((self.x, self.y))

    def __str__(self):
        return str((self.x, self.y))

    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other, self.y - other)

    def __divmod__(self, other):
        print(type(self), type(other))
        if type(other) == Vector:
            return Vector(self.x / other.x, self.y / other.y)
        else:
            return Vector(self.x / other, self.y / other)

    def __mul__(self, other):
        if type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    def normalize(self, future):
        pos = (self.x, self.y)

        dist = (self.x**2 + self.y**2) ** 0.5
        return self.x/dist, self.y/dist

    def get_tuple(self):
        return self.x, self.y


# oct cell
class Cell:
    def __init__(self, x, y, color):
        self.pos = Vector(x, y)
        self.color = color


class Tile:
    def __init__(self):
        self.type = "undefined"  # undefined, city, road, forest, water
        self.color = [0, 0, 0]

    @property
    def cell_color(self):
        if self.type == "undefined":
            return self.color
        if self.type == "road":
            return render_road_color
        if self.type == "forest":
            return render_forest_color
        if self.type == "water":
            return render_water_color
        if self.type == "city":
            return render_city_color


def cos(deg):
    return math.cos(deg/180*math.pi)


def sin(deg):
    return math.sin(deg/180*math.pi)


def sqrt(n):
    return n**0.5
