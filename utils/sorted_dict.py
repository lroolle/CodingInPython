
from collections import OrderedDict


def sorted_dict(d, keys):
    """ Sort dict according to keys list
    >>>keys = ['d', 'c', 'b', 'a']
    >>>d = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
    >>>sorted_dict(d, keys)
    >>>OrderedDict([('d', 4), ('c', 3), ('b', 2), ('a', 1), ('e', 5), ('g', 7), ('f', 6)])
    """
    d_size = len(d)
    return OrderedDict(
        sorted(d.items(),
               key=lambda x: keys.index(x[0]) if x[0] in keys else d_size)
    )