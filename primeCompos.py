import math
#n != 2k**2 + p
def isPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    for i in range(2, num//2):
        if (num % i) == 0:
            return False
    return True

def isPerfSquare(num):
    perfSquare = math.sqrt(num / 2)
    return (perfSquare == round(perfSquare))


def main():
    n = 1
    found = True
    primes = list(filter(lambda num: num != 0, [(i * isPrime(i)) for i in range(10000)]))
        
    while not found:
        n += 2

        if (n % 2) == 0:
            print (f"It is not {n}")
            continue

        i = 0
        found = True
        while primes[i] <= n:
            if isPerfSquare(n - primes[i]):
                print (f"It is not {n}")
                found = False
                break
            i += 1
    print(n)

if __name__ == '__main__':
    main()