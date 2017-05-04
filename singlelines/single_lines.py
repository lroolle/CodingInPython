#!usr/local/env python3


"""Python Single Line TIPS

> Inspired By 「 一行 Python 能实现什么丧心病狂的功能？ 」
> (https://www.zhihu.com/question/37046157)

"""


def filter_primes(n):
    return filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, n))
    # NOTE: In python3 this returns a 'filter object' which is a
    # iterator instead of lists


def is_prime(num):
    pass


def read_file():
    with open('t.csv', 'r') as f:
        rows = [line.strip().split(',') for line in f.readlines()]
    return rows


def sort_array(a):
    return sorted(a, key=lambda x: x[1], reverse=True)[:10]


def str_xor(s1, s2):
    return ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(s1, s2)])


def dict_list(l):
    return {i: x for i, x in enumerate(l) if i % 2 == 0}
