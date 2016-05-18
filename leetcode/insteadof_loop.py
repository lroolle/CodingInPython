def print_without_loop(n):
    print(n)
    if n == 1000:
        return

    return print_without_loop(n + 1)


def print_without_loop2(n):
    print(list(range(n + 1)))

print_without_loop2(1000)
