import math

#n != 2k**2 + p

def isPrime(num):
    if num == 1 or num == 0 or num == 2:
        return False
    divisors = []
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def main():
    n = 0
    found = False
    while not found:
        if (n % 2) == 0:
            print(f"It is not {n}")
            n += 1
            continue

        if isPrime(n):
            print(f"It is not {n}")
            n += 1
            continue

        for i in range(1, n):
            for j in range(1, n):
                if not isPrime(j):
                    continue
                if not ((2 * (i ** 2)) + j == n):
                    print(f"It is {n}")
                    found = True
                    break
            if found:
                break
        n += 1
                

if __name__ == '__main__':
    main()