# insertion_sort.py


def insertion_sort1(a):
    for i in range(1, len(a)):
        j = i
        tmp = a[i]

        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1

        a[j] = tmp

    return a


# enumerate
def insertion_sort2(a):
    for i, item in enumerate(a):
        j = i

        while j > 0 and item < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1

        a[j] = item

    return a
