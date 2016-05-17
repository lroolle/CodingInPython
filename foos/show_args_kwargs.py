def show_args(*args):
    print(args)


def show_kwargs(**kwargs):
    print(kwargs)


def show_both(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    show_args(1, '2', 'hello args', [1, 2, 'args'])
    # (1, '2', 'hello args', [1, 2, 'args'])
    show_kwargs(a=1, b='2', c='hello kwargs', d=[1, 2, 'kwargs'])
    # {'b': '2', 'c': 'hello kwargs', 'd': [1, 2, 'kwargs'], 'a': 1}
    show_both('hello args', [1, 2, 'args'], c='hello kwargs', d=[1, 2, 'kwargs'])
# ('hello args', [1, 2, 'args']) {'c': 'hello kwargs', 'd': [1, 2, 'kwargs']}
