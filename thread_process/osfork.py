
import os


def test_fork():
    pid = os.fork()
    if pid == 0:
        print('child')
        os._exit(0)
    else:
        print('parent')


if __name__ = 'main':
    test_fork()
