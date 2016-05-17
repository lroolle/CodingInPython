class ClassDecorator:
    def __init__(self, func):
        print('__init__: Initialize ClassDecorator')
        self.func = func

    def __call__(self):
        print('__call__: Call function')
        self.func()


@ClassDecorator
def func():
    print('I\'m a function, Come on Decorate me !')


func()
print('Finish decorate func')
# >>> __init__: Initialize ClassDecorator
# >>> __call__: Call function
# >>> I'm a function, Come on Decorate me !
# >>> Finish decorate func
