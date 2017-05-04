# heap_sort.py
# Priority Queues


def sift_down(a, start, end):
        """最大堆调整

        :param a: Array
        :param start: Start point
        :param end: End point
        """
        root = start
        while 1:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break


def heap_sort(a):
    # 创建最大堆
    for start in range((len(a) - 2) // 2, -1, -1):
        sift_down(a, start, len(a) - 1)

    # 堆排
    for end in range(len(a) - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end - 1)

    return a
