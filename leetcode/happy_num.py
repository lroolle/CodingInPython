def is_happy(n):
    if n == 1:
        return True

    if n <= 4:
        return False

    sums = 0

    while n / 10 > 0:
        sums += (n % 10) ** 2
        n //= 10

    return is_happy(sums)


print(is_happy())
