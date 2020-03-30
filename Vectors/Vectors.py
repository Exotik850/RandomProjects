import math
import random


class Vector:

    def __init__(self, x, y):
        if x and y:
            self.x = x
            self.y = y
            self.heading = math.atan2(y, x)
        else:
            self.x = 0
            self.y = 0

    def __add__(self, som):
        try:
            self.x = self.x + som.x
            self.y = self.y + som.y
            return self
        except:
            return Vector(self.x + som, self.y + som)

    def __sub__(self, som):
        try:
            self.x = self.x - som.x
            self.y = self.y - som.y
            return self
        except:
            return Vector(self.x - som, self.y - som)

    def div(self, som):
        self.x /= som
        self.y /= som
        return self

    def __iadd__(self, som):
        return self + som

    def __mul__(self, num):
        self.x *= num
        self.y *= num
        return self

    def __str__(self):
        return f'{self.x}, {self.y}'

    __repr__ = __str__

    def rotate(self, r):
        newH = self.heading + r
        # if newH == newH * (180 / math.pi):
        mag = self.mag()
        self.x = math.cos(newH) * mag
        self.y = math.sin(newH) * mag
        self.heading = newH
        return self

    def remainder(self, other):
        pass

    def cross(self, other):
        return (self.x * other.y - self.y * other.x)

    def copy(self):
        return self

    def dot(self, vector):
        return ((self.x * vector.x) + (self.y * vector.y))

    def mag(self):
        return math.sqrt(self.magSq())

    def magSq(self):
        return (self.x * self.x + self.y * self.y)

    def setMag(self, n):
        return self.normalize() * n

    def limit(self, n):
        mag = self.mag()
        if mag > n:
            self.setMag(n)
            return self
        else:
            return self

    def normalize(self):
        m = self.mag()
        if not (m == 0):
            self = self.div(m)
            return self
        else:
            return 0

    @staticmethod
    def random2D():
        return Vector(random.uniform(-1, 1), random.uniform(-1, 1))
