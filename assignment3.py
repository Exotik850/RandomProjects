import math

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
    return [sum([i[0] for i in [[val1, val2, val3] for val1, val2, val3 in vectors]]), sum([i[1] for i in [[val1, val2, val3] for val1, val2, val3 in vectors]]), sum([i[2] for i in [[val1, val2, val3] for val1, val2, val3 in vectors]])]

def find_line(a, b):
    return "y = " + str(round((b[1] - a[1]) / (b[0] - a[0]), 2)) + "x + " + str(round(a[1] - round((b[1] - a[1]) / (b[0] - a[0]), 2) * a[0], 2))

def barbell_centroid(left, right):
    return "Error" if left > 10 or right > 10 else ((sum([(45 * ((-2 * i - 1) - 25)) for i in range(0, left)]) + sum([(45 * ((2 * i + 1) + 25)) for i in range(0, right)])) / ((left + right) * 45))

print(vector_add((2, 1, 3), (1, 1, 1)))
        