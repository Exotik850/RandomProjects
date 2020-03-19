from functools import lru_cache

#Fibonacci Sequence
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n - 2)

#Towers of Hanoi
output = open("hanoiForXDiscs.txt", "w")
def move(frompl, dest):
    output.write(f"Move {frompl} to {dest} \n")

def hanoi(num, frompl, via, dest):
    if num == 0:
        pass
    else:
        hanoi(num-1, frompl, dest, via)
        move(frompl, dest)
        hanoi(num-1, via, frompl, dest)

#Minimum number of boxes can be put into a set width and height
def areaTiles(w, h):
    if w == 0 or h == 0:
        return 0
    elif w % 2 == 0 and h % 2 == 0:
        return areaTiles(int(w / 2), int(h / 2))
    elif w % 2 == 0 and h % 2 == 1:
        return w + areaTiles(int(w / 2), int(h / 2))
    elif w % 2 == 1 and h % 2 == 0:
        return h + areaTiles(int(w / 2), int(h / 2))
    else:
        return w + (h - 1) + areaTiles(int(w / 2), int(h / 2))

