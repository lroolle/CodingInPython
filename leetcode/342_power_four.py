"""LeetCode 342. Power of Four

> Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""

import re


def is_power_four(num):
    return num > 0 and num & (num - 1) == 0 and num & 0x55555555 > 0


def is_power_four2(num):
    return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0


def is_power_four3(num):
    if num == 1:
        return True

    b = '{0:b}'.format(num)
    if re.match(r'^1(00)+$', b):
        return True

    return False


for i in range(100):
    print(i, is_power_four(i))
    print(i, is_power_four2(i))
    print(i, is_power_four3(i))
