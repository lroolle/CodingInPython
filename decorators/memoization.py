"""

"""


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


# Or whats more


def cls_memoize(f):

    class Memo(dict):

        def __init__(self, func):
            self.f = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return Memo(f)
