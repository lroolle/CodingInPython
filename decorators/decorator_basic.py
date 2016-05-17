def mark_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def mark_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@mark_bold
@mark_italic
def hello():
    return "hello dumb decorators"


# print(hello())


# returns "<b><i>hello dumb decorators</i></b>"


def decorate(fn):
    print('111')
    fn()
    print('333')


@decorate
def hahhah():
    print('222')
