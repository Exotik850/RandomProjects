import math

pi = math.pi

def my_atan(y, x):
    return math.atan(y/x) if x > 0 else math.atan(y/x + pi) if y >= 0 and x < 0 else math.atan(y/x - pi) if y < 0 and x < 0 else pi/2 if y > 0 and x == 0 else -pi/2 if y < 0 and x == 0 else 0

def vector_add(*vectors):
    return [sum([i[0] for i in [[val1, val2, val3] for val1, val2, val3 in vectors]]), sum([i[1] for i in [[val1, val2, val3] for val1, val2, val3 in vectors]]), sum([i[2] for i in [[val1, val2, val3] for val1, val2, val3 in vectors]])]

def find_line(a, b):
    return "y = " + str(round((b[1] - a[1]) / (b[0] - a[0]), 2)) + "x + " + str(round(a[1] - round((b[1] - a[1]) / (b[0] - a[0]), 2) * a[0], 2))

def barbell_centroid(left, right):
    return "Error" if left > 10 or right > 10 else ((sum([(45 * ((-2 * i - 1) - 25)) for i in range(0, left)]) + sum([(45 * ((2 * i + 1) + 25)) for i in range(0, right)])) / ((left + right) * 45))

def is_barbell_stable(left, right):
    return False if barbell_centroid(left, right) < -25 or barbell_centroid(left, right) > 25 else True

def cramers_rule(A, b):
    return "Error" if len(b) != len(A) else (((b[0] * A[1][1]) - (A[0][1] * b[1])) / ((A[0][0] * A[1][1]) - (A[0][1] * A[1][0]))), (((A[0][0] * b[1]) - (b[0] * A[1][0])) / ((A[0][0] * A[1][1]) - (A[0][1] * A[1][0])))