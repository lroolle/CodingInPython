"""LeetCode 345. Reverse Vowels of a String

> Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Given s = "hello", return "holle".

Example 2:

Given s = "leetcode", return "leotcede".
"""


def reverse_vowels(s):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    l, u = 0, len(s) - 1
    sl = list(s.lower())

    while 1:
        if l >= u:
            break

        while sl[l] not in VOWELS and l < u:
            l += 1

        while sl[u] not in VOWELS and l < u:
            u -= 1

        sl[l], sl[u] = sl[u], sl[l]
        l, u = l + 1, u - 1

    return ''.join(sl)


print(reverse_vowels('aeiouaeiou'))
# >>> uoieauoiea
