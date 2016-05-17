def print_without_loop(n):
    print(n)
    if n == 1000:
        return

    return print_without_loop(n + 1)


print_without_loop(1)