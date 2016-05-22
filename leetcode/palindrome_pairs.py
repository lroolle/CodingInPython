#!usr/bin/env python3


"""LeetCode 336. Palindrome Pairs

> Given a list of unique words. Find all pairs of distinct
indices (i, j) in the given list, so that the concatenation
of the two words, i.e. words[i] + words[j] is a palindrome.

- Example 1:

    Given words = ["bat", "tab", "cat"]
    Return [[0, 1], [1, 0]]
    The palindromes are ["battab", "tabbat"]

- Example 2:

    Given words = ["abcd", "dcba", "lls", "s", "sssll"]
    Return [[0, 1], [1, 0], [3, 2], [2, 4]]
    The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

"""


def is_palindrome(s):
    length = len(s)
    for i in range(length // 2 + 1):
        if s[i] != s[-(i + 1)]:
            return False

    return True


def palindrome_pairs(l):
    res = list()
    for i, item in enumerate(l):
        for j in range(i + 1, len(l)):
            if is_palindrome(item + l[j]):
                res.append([i, j])
            if is_palindrome(l[j] + item):
                res.append([j, i])

    return res


def palindrome_pairs2(l):
    pass


print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
