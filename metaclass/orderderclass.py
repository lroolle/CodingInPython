import collections


class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result


class A(metaclass=OrderedClass):
    def one(self): print(1)

    def two(self): print(2)

    def three(self): print(3)

    def four(self): print(4)


print(A.members)
# ('__module__', '__qualname__', 'one', 'two', 'three', 'four')
