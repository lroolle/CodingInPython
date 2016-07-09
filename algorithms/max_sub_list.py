"""Max sub list


"""


def max_sub_list(l):
    best = cur = 0
    for x in l:
        cur = max(cur + x, 0)
        best = max(best, cur)
    return best


def max_sub_list2(lst):
    sum = 0
    b = 0
    for i in range(len(lst)):
        if b > 0:
            b += lst[i]
        else:
            b = lst[i]
        if b > sum:
            sum = b
    return sum


print(max_sub_list([-6, 0, -6, 2, -1, 9, 1]))
print(max_sub_list2([-6, 0, -6, 2, -1, 9, 1]))
