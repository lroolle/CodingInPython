# foo.py


def foo(a, l, r):
    if l < r:
        foo(a, l + 1, r - 1)
        a[l], a[r] = a[r], a[l]


a = [1, 2, 3, 4, 5, 6]

for x in range(6):
    print(a[x])
