"""LeetCode 357. Count Numbers with Unique Digits

> Given a non-negative integer n, count all numbers with unique digits, x,
where 0 ≤ x < 10 ^ n.

- Example:
    Given n = 2, return 91. (The answer should be the total numbers in the range
    of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

"""


def count_digits(n):
    count = 0
    for i in range(10 ** n):
        digits_list = list(str(i))
        if len(set(digits_list)) == len(digits_list):
            count += 1

    return count


def count_digits2(n):
    if n == 1:
        return 10
    elif n == 0:
        return 1
    elif n > 10 or n <= 0:
        return 0
    a, b = 9, 10
    for i in range(2, n + 1):
        a *= (11 - i)
        b += a
    return b


print(count_digits(2))
