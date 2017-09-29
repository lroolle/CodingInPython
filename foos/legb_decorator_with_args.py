
import functools


def decorator(tag):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return "<%s> %s </%s>" % (tag, func(*args, **kwargs), tag)
        return wrapper
    return dec



@decorator( 'xxx' )
def test2():
    return 'test1XML'


if __name__ == '__main__':
    print(test2())



