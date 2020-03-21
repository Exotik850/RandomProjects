import math
import time
from functools import lru_cache
#n != 2k**2 + p

def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def isPerfSquare(num):
    perfSquare = math.sqrt(num / 2)
    return (perfSquare == round(perfSquare))

@lru_cache(maxsize=1000)
def main():
    n = 1
    found = False
        
    startTime = time.time()
    primes = list(filter(lambda num: num != 0, [(i * isPrime(i)) for i in range(6000)]))   
    while not found:
        n += 2

        if isPrime(n):
            continue

        i = 0
        found = True
        while n >= primes[i]:
            if isPerfSquare(n - primes[i]):
                found = False
                break
            i += 1
    print(f"It is {n}")
    print(f"Done in {round(time.time() - startTime, 2)} second(s)")

if __name__ == '__main__':
    main()