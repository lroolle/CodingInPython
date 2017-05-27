""" LEVEL 3-1 
05,23 2017 https://www.google.com/foobar/?user=wrqatw


Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need 
access to it. But the only door leading to the LAMBCHOP chamber is secured 
with a unique lock system whose number of passcodes changes daily. Commander 
Lambda gets a report every day that includes the locks' access codes, 
but only she knows how to figure out which of several lists contains the 
access codes. You need to find a way to determine which list contains the 
access codes once you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, 
she's confided to you that she made all the access codes "lucky triples" in 
order to help her better find them in the lists. A "lucky triple" is a tuple 
(x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that 
information, you can figure out which list contains the number of access 
codes that matches the number of locks on the door when you're ready to go in 
(for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky 
triple" access codes).

Write a function answer(l) that takes a list of positive integers l and 
counts the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j 
< k.  The length of l is between 2 and 2000 inclusive.  The elements of l are 
between 1 and 999999 inclusive.  The answer fits within a signed 32-bit 
integer. Some of the lists are purposely generated without any access codes 
to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: 
[1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) l = [1, 1, 1]
Output:
    (int) 1

Inputs:
    (int list) l = [1, 2, 3, 4, 5, 6]
Output:
    (int) 3
"""

from itertools import combinations


def my_combinations(l, r=3):
    pool = tuple(l)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def lucky_triples(l):
    """Return the set of distinct triples x, y, z from an iterable of
    numbers, such that x <= y <= z and x divides y and y divides z.

    """
    return len(set((x, y, z)
               for x, y, z in combinations(sorted(l), 3)
               if y % x == 0 and z % y == 0))


def lucky_triple_count(l):
    c = 0
    for x, y, z in combinations(l, 3):
        if not y % x == 0 or not z % y == 0:
            continue
        c += 1
    return c


def answer(l):
    c = 0
    for i, lucky0 in enumerate(l):
        for j, lucky1 in enumerate(l[i + 1:]):
            if not lucky1 % lucky0 == 0:
                continue

            k = j + i + 2
            for lucky2 in l[k:]:
                if lucky2 % lucky1 == 0:
                    c += 1
    return c


def my_answer(l):
    c, l_len = 0, len(l)
    d = [l_len]

    for i in range(2, l_len):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                d[i] += 1
    for i in range(2, l_len):
        for j in range(2, i):
            if l[i] % l[j] == 0:
                c += d[j]

    return c


from bisect import insort_left


def answer1(l):

    indices = {}
    setdefault_ = indices.setdefault
    for i, x in enumerate(l):
        setdefault_(x, []).append(i)

    out = 0
    highest_value = max(l)
    for i, x in enumerate(l):
        multiples = []
        for m in range(1, int(highest_value / x) + 1):
            if x * m in indices:
                for j in indices[x * m]:
                    if i < j:
                        insort_left(multiples, (j, x * m))

        if multiples:
            multiples = [m[1] for m in multiples]
            for pair in combinations(multiples, 2):
                out += pair[1] % pair[0] == 0

    return out


def answer2(l):
    c, s,  = list(), len(l)
    n = s * [0]
    for i in range(1, s - 1):
        for j in range(i):
            if not l[i] % l[j] == 0:
                continue
            n[i] += 1

    for i in range(2, s):
        for j in range(1, i):
            if not l[i] % l[j] == 0:
                continue
            c.append(n[j])

    return sum(c)
