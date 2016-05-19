def count_ones_r(num):
    if num < 2:
        return num
    print(num)

    return num % 2 + count_ones_r(num // 2)


print("xx_x", count_ones_r(125))
