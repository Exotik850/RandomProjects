import math

pi = math.pi
def atan2(y, x):
    if x > 0:
        return math.atan(y/x)
    elif y >= 0 and x < 0:
        return math.atan(y/x + pi)
    elif y < 0 and x < 0:
        return math.atan(y/x - pi)
    elif y > 0 and x == 0:
        return pi/2
    elif y < 0 and x == 0:
        return -pi/2
    else:
        return 0

def radians_to_degrees(radians):
    return radians * (180 / pi)
x = int(input('x: '))
y = int(input('y: '))
print(atan2(y, x))
print(radians_to_degrees(atan2(y, x)))