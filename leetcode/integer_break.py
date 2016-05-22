#!usr/bin/env python3


"""LeetCode 343. Integer Break

> Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.

Hint:

- There is a simple O(n) solution to this problem.
- You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

"""


def integer_break(n):
    """O(1) Solution

    :param n:
    :return:
    """
    div = n // 3

    if div <= 1:
        return (n // 2) * (n // 2 + n % 2)

    mod = n % 3

    if mod == 0:
        return 3 ** div
    if mod == 1:
        return 3 ** (div - 1) * 4
    if mod == 2:
        return 3 ** div * 2


def integer_break2(n):
    """动态规划 O(n)
    dp[i]表示整数i拆分可以得到的最大乘积，则dp[i]只与dp[i - 2], dp[i - 3]两个状态有关,
    得到状态转移方程：
        dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])

    :type n: int
    :rtype: int
    """
    if n <= 3:
        return n - 1

    dp = [0] * (n + 1)
    dp[2], dp[3] = 2, 3
    for x in range(4, n + 1):
        dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
    return dp[n]


for i in range(2, 101):
    print(i, integer_break(i))
    # print(i, integer_break2(i))

# 2 1
# 3 2
# 4 4
# 5 6
# 6 9
# 7 12
# 8 18
# 9 27
# 10 36
# ...
