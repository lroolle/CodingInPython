""" Python yield and return
"""


def foo(n):
    """
    >>> list(foo(0))
    []
    >>> list(foo(1))
    []
    >>> list(foo(2))
    [0, 2]
    """
    if n in (0, 1):
        return [1]
    for item in range(n):
        yield item * 2


def yaha(n):
    """
    >>> list(yaha(0))
    [0]
    >>> list(yaha(1))
    [1, 0]
    >>> list(yaha(2))
    [0, 2]

    """
    if n in (0, 1):
        yield n
    for item in range(n):
        yield item * 2


def bar(n):
    """
    >>> list(bar(0))
    [0]
    >>> list(bar(1))
    [1]
    >>> list(bar(2))
    [0, 2]
    """
    if n in (0, 1):
        yield n
    else:
        for item in range(n):
            yield item * 2




