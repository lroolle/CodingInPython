# selection_sort.py


def selection_sort(a):
    for i in range(len(a)):
        min = i

        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j

        a[min], a[i] = a[i], a[min]

    return a
