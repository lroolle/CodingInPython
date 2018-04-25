from decorators import memoization


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def test0(n):
    fib(n)


def test1(n):

    @memoization.memoize
    def fib1(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    fib1(n)


def test2(n):
    @memoization.cls_memoize
    def fib2(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    fib2(n)


