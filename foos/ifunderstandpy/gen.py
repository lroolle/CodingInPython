

class Foo(object):
    x = 1
    bad_gen = (x for _ in range(10))
    lambda_gen = (lambda x: (x for _ in range(10)))(x)
    foo_gen = (Foo.x for _ in range(10))

    @classmethod
    def gen(cls):
        for _ in range(10):
            yield cls.x


if __name__ == '__main__':
    # x = 1
    # print(list((x for _ in range(5))))
    # print(Foo.gen)
    # foo = Foo()
    print('Holy Girl', list(Foo.gen()))
    print('MR Lambda', list(Foo.lambda_gen))
    print('Bar Foo', list(Foo.foo_gen))
    print('Apple Bad', list(Foo.bad_gen))
