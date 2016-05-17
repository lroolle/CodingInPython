"""If you can type those keys:'a', 'c', 'v', 'Ctrl' for several times;

    Find a way to output the most number of 'a'.

"""


def most_a():

    for p in range(1, 100):

        max_a = {i: 2 ** int((p - i)/6) * i for i in range(1, p + 1)}
        print(max_a)

    return max_a


print(most_a())