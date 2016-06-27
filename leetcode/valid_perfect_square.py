"""LeetCode 367. Valid Perfect Square

> Given a positive integer num, write a function which returns True if num is a
perfect square else False.

Note: Do not use any built-in library function such as sqrt.

- Example 1:

Input: 16
Returns: True

- Example 2:

Input: 14
Returns: False

"""


def is_perfect(num):
    """Newton's Method

    :param num:
    :return:
    """
    x = num
    while x ** 2 > num:
        x = (x + num // x) // 2

    return x ** 2 == num


def is_perfect2(num):
    """A perfect Square num can be divided into:
       1 + 3 + 5 + 7 + ...

    :param num:
    :return:
    """
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


print(is_perfect(14))
print(is_perfect2(14))
print(is_perfect(16))
print(is_perfect2(16))
