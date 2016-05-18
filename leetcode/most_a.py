"""If you can type those keys: 'a', 'c', 'v', 'Ctrl' for several times;

    Find a way to output the most number of 'a'.
"""


def most_a(n):
    max_a = {}
    for p in range(1, n + 1):
        max_a = {i: 2 ** ((p - i) // 6) * i for i in range(1, p + 1)}
    max_a_sort = sorted(max_a.items(), key=lambda x: x[1], reverse=True)

    return max_a_sort[0], (n - max_a_sort[0][0]) // 6


for i in range(1, 100):
    print(i, most_a(i))
