# bubble_sort.py


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(1, len(a) - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

    return a
