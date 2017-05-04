# merge_sort.py


def merge(left, right):
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]

    return result


def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) >> 1
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)
