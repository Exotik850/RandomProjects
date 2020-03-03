import math
import operator
pi = math.pi

def my_atan(y, x):
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

def vector_add(*vectors):
    v1, v2, v3 = [], [], []
    end1, end2, end3 = 0, 0, 0
    for i in vectors:
        v1.append(i[0])
        v2.append(i[1])
        v3.append(i[2])
    for val1, val2, val3 in zip(v1, v2, v3):
        end1 += val1
        end2 += val2
        end3 += val3
    return [end1, end2, end3]

def find_line(a, b):
    slope = round((b[1] - a[1]) / (b[0] - a[0]), 2)
    y_int = round(a[1] - slope * a[0], 2)
    return "y = " + str(slope) + "x + " + str(y_int)

def barbell_centroid(left, right):
    if left > 10 or right > 10:
        return "Error"
    x_left = (-(left / 2) - 25) * 45
    x_right = ((right / 2) + 25) * 45
    return (x_left + x_right) / ((left + right) * 45)
print(barbell_centroid(10, 1))
        