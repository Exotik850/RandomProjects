
def perf(n):
    global ct
    ct += 1
    if len(str(n)) == 1:
        return 0
    digits = [i for i in str(n)]
    result = 1
    for i in digits:
        result *= int(i)
    perf(result)

maxStep = 0
maxNum = 0
i = 0

while True:
    ct = 0
    perf(i)
    if ct - 1> maxStep:
        maxStep = ct - 1
        maxNum = i
        print(f"{maxNum}: {maxStep}")
    i += 1