# shell_sort.py


def shell_sort(a):
    gap = len(a)

    # gap = gap // 2
    while gap > 0:
        gap >>= 1

        for i in range(gap, len(a)):
            j = i
            tmp = a[i]

            while j >= gap and tmp < a[j - gap]:
                a[j] = a[j - gap]
                j -= gap

            a[j] = tmp

    return a
