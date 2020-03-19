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
