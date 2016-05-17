import math


def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))


def get_primes2(n):
    p = 2
    count = 0
    while count < n:
        if is_prime(p):
            yield p
            count += 1
        p += 1


def print_primes(n):
    prime_generator = get_primes2(n)
    t = []
    for p in prime_generator:
        t.append(p)

    return t


if __name__ == '__main__':
    # print_successive_primes(6)
    import timeit

    timeit.timeit(print_primes(10000))
