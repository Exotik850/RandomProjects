import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heading = math.atan2(y, x)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def mult(self, num):
        self.x *= num
        self.y *= num

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)