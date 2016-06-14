#!urs/bin/env python3


import time


def foo(x):
    print('11111')
    do_something(x)
    print('23333')
    return 0


def do_something(x):
    print(x)
    time.sleep(5)


foo(0)
