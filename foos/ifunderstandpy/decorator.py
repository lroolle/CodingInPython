import time


class timeit(object):

    def __init__(self, f):
        self._wrapped = f

    def __call__(self, *args, **kwargs):
        s = time.time()
        ret = self._wrapped(*args, **kwargs)
        e = time.time()
        print(self._wrapped.__name__, 'Aha: %d' % (e - s))
        return ret

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self._wrapped(instance, *args, **kwargs)


class Foo(object):

    @timeit
    def f(self):
        print('fFF...')
        time.sleep(2)

    @classmethod
    @timeit
    def ff(self):
        print('f2F...')
        time.sleep(2)


@timeit
def foo():
    print('zZZ...')
    time.sleep(2)


if __name__ == '__main__':
    foo()

    Foo.ff()

    # TypeError: f() missing 1 required positional argument: 'self'
    # 等同于 timeit(ifoo.f)()
    ifoo = Foo()
    ifoo.f()

