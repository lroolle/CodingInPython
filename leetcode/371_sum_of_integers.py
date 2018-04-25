"""LeetCode 371. Sum of 2 Integers
> Calculate the sum of two integers a and b, but you are not allowed to use
the operator + and -.

- Example:
Given a = 1 and b = 2, return 3.
"""


def sum_of_integers(a, b):
    return sum([a, b])


def recursive_sum(a, b):
    r, c = a ^ b, a & b
    return r if c == 0 else recursive_sum(r, c << 1)


def loop_sum(a, b):
    r, c = a ^ b, a & b
    while c:
        c <<= 1
        tmp = r
        r ^= c
        c &= tmp

    return r


if __name__ == '__main__':
    import random
    for i in range(10000):
        a, b = random.randint(0, 10000), random.randint(0, 10000)
        x = sum_of_integers(a, b)
        y = recursive_sum(a, b)
        z = loop_sum(a, b)
        assert x == y == z, '{}, {}, {}'.format(x == y, x == z, y == z)
        print('Ok')

