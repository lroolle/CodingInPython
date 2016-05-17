# quick_sort.py


def qsort1(a):
    """Out-in-place quick sort

    :param a: unsorted array
    :return: sorted
    """
    if len(a) <= 1:
        return a

    return qsort1([x for x in a[1:] if x < a[0]]) + \
            [a[0]] + \
            qsort1([x for x in a[1:] if x >= a[0]])


def qsort2(a):
    """Unofficial

    :param a: unsorted array
    :return: a generator to generate sorted array
    """
    if not a:
        return []

    elif len(a) == 1:
        yield a[0]

    else:
        yield from qsort2([x for x in a if x < a[0]])
        yield from [x for x in a if x == a[0]]
        yield from qsort2([x for x in a if x > a[0]])


def qsort3(a, l, u):
    """In-place quick sort
    One index for partition

    :param a: unsorted array
    :param l: lower bound
    :param u: upper bound
    :return: None
    """
    if l >= u:
        return

    m = l

    for i in range(l + 1, u + 1):
        if a[i] < a[l]:
            m += 1
            a[m], a[i] = a[i], a[m]

    a[m], a[l] = a[l], a[m]
    qsort3(a, l, m - 1)
    qsort3(a, m + 1, u)


def qsort4(a, l, u):
    """In-place quick sort
    Two index for partition

    :param a: unsorted array
    :param l: lower bound
    :param u: upper bound
    :return: None
    """
    if l >= u:
        return

    pivot = a[l]
    left, right = l + 1, u

    while left <= right:
        while left <= right and a[left] < pivot:
            left += 1
        while left <= right and a[right] >= pivot:
            right -= 1
        if left > right:
            break

        a[left], a[right] = a[right], a[left]

    a[l], a[right] = a[right], a[l]
    qsort4(a, l, left - 1)
    qsort4(a, right + 1, u)

# def test(seq, n):
#     it = iter(seq)
#     return [next(it, None) for _ in range(n)]

# print(qsort2([2, 1, 3, 5], 0, 3))


# if __name__ == '__main__':
# for i in qsort1([8, 1, 3, 4, 56, 7, 8, 5, 5, 76]):
#     print(i)

#
# import random
# array = [random.randint(0, 10) for _ in range(10)]
# print('---', array, '---')
# qsort3(array, 0, len(array) - 1)
# print(array)
