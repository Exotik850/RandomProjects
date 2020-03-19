import time


def move(frompl, dest):
    output.write(f"Move {frompl} to {dest} \n")

def hanoi(num, frompl, via, dest):
    if num == 0:
        pass
    else:
        hanoi(num-1, frompl, dest, via)
        move(frompl, dest)
        hanoi(num-1, via, frompl, dest)

output = open("hanoiFor25Discs.txt", "w")
startTime = time.time()
hanoi(25, "A", "B", "C")
print(f"Done in {round(time.time() - startTime, 2)} second(s)")