import itertools


def zip_list(list1, list2):
    return [x for x in itertools.chain.from_iterable(itertools.zip_longest(
        list1, list2))]
