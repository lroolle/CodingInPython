

def fact(n, product):

    if n <= 1:
        return 1
    else:
        return fact(n - 1, n * product)


if __name__ == "__main__":
    fact(10000)
