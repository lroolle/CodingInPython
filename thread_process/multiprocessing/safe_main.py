
"""
Safe importing of main module

Make sure that the main module can be safely imported by a new Python interpreter without causing unintended side effects (such a starting a new process).

For example, using the spawn or forkserver start method running the following module would fail with a RuntimeError:
"""

from multiprocessing import Process

def foo():
    print('hello')

p = Process(target=foo)
p.start()

"""
Instead one should protect the “entry point” of the program by using if ``__name__ == '__main__'``: as follows:
"""

from multiprocessing import Process, freeze_support, set_start_method

def foo():
    print('hello')

if __name__ == '__main__':
    freeze_support()
    set_start_method('spawn')
    p = Process(target=foo)
    p.start()

"""
(The freeze_support() line can be omitted if the program will be run normally instead of frozen.)

This allows the newly spawned Python interpreter to safely import the module and then run the module’s foo() function.

Similar restrictions apply if a pool or manager is created in the main module.
"""

