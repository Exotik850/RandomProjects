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
            tempv = Vector(0, 0)
            tempv.x = self.x + som.x
            tempv.y = self.y + som.y
            return tempv 
        except:
            return Vector(self.x + som, self.y + som)
    
    def __iadd__(self, som):
        try:
            tempv = Vector(0, 0)
            tempv.x = self.x + som.x
            tempv.y = self.y + som.y
            return tempv 
        except:
            return Vector(self.x + som, self.y + som)

    def mult(self, num):
        try:
            tempv = Vector(0, 0)
            tempv.x = self.x * num.x
            tempv.y = self.y * num.y
            return tempv 
        except:
            return Vector(self.x * num, self.y * num)

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def rotate(self, r):
        temp = self
        r *= math.pi / 180
        self.x = round(math.cos(temp.x * r) - math.sin(temp.y * r), 3)
        self.y = round(math.sin(temp.x * r) + math.cos(temp.y * r), 3)
        self.heading = math.atan2(self.y, self.x)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        
    def dot(self, vector):
        return ((self.x * vector.x) + (self.y * vector.y))

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def magSq(self):
        return (self.x * self.x + self.y * self.y)

    def cross(self, other):
        return (self.x * other.y - self.y * other.x)

    @staticmethod
    def random2D():
        return Vector(random.uniform(-1, 1), random.uniform(-1, 1))

    