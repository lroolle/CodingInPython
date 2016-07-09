# binary_search.py


def binary_search(a, key):
    a.sort()
    print(a)
    l = 0
    u = len(a) - 1

    while l < u:
        mid = l + (u - l) // 2
        if key < a[mid]:
            u = mid + 1
        elif key > a[mid]:
            l = mid - 1
        else:
            return mid

    return

print(binary_search([1, 5, 8, 3, 9], 3))
