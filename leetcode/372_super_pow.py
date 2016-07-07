"""LeetCode 372. Super pow

> Your task is to calculate a ^ b mod 1337 where a is a positive integer and
b is an extremely large positive integer given in the form of an array.

- Example1:
a = 2
b = [3]
Result: 8

- Example2:
a = 2
b = [1,0]
Result: 1024
"""


def super_pow(a, b):
    b_str = ''
    for x in b:
        b_str += str(x)

    b = int(b_str)
    return a ** b % 1337


print(super_pow(2, [1, 0]))
