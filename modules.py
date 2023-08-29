import math


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


def cos(deg):
    return math.cos(deg/180*math.pi)


def sin(deg):
    return math.sin(deg/180*math.pi)


def sqrt(n):
    return n**0.5
