import math
import random

def generate_keys():
    p1 = get_random_prime()
    p2 = get_random_prime()
    if p1 == p2:
        return generate_keys()

    n = p1 * p2
    phiN = (p1 - 1) * (p2 - 1)

    e = get_random_prime()
    if e < 1 or e >= phiN:
        return generate_keys()

    d = calculate_d(e, phiN)
    if d == -1:
        return generate_keys()

    return {"n": n, "e": e, "d": d}

def calculate_d(e, phiN):
    k = 1
    d = (k * phiN + 1) / e
    while d != math.floor(d):
        if k > 1000:
            return -1
        k += 1
        d = (k * phiN + 1) / e
    return int(d)

def get_random_prime():
    prime_numbers = prime_sieve(100)
    prime = prime_numbers[random.randint(5, len(prime_numbers)-1)]
    return prime

def prime_sieve(max):
    numbers = [i for i in range(0, max)]
    for x in range(2, math.floor(max/2)):
        for y in range(x+1, max):
            if y / x == math.floor(y / x):
                numbers[y] = 0
    prime_numbers = [n for n in numbers if n != 0]
    return prime_numbers
