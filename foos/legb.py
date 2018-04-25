

def foo(arg1):
    """TODO: Docstring for foo.
    :returns: TODO

    """
    def bar(arg2):
        def foobar(arg3):
            print(arg1)
            print(arg2)
            print(arg3)
        foobar('23333')
    bar('2333')
foo('233')

