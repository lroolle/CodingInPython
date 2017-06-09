""" Function @property in a function
> http://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/bs4/element.py?start_revid=342#L1435
"""


def _alias(attr):
    """ Alias one attribute name to another for backward compatibility
    """

    @property
    def alias(self):
        return getattr(self, attr)

    @alias.setter
    def alias(self):
        return setattr(self, attr)
    return alias


class Foo(object):

    def __init__(self):
        self.bar = None

    _alias('bar')


foo = Foo()
print(foo.__dict__)
## 莫名其妙

