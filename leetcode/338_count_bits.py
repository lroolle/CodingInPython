"""LeetCode 338. Count Bits

> Given a non negative integer number `num`. For every numbers i in the
range `0 ≤ i ≤ num` calculate the number of 1's in their binary
representation and return them as an array.

- Example:
For `num = 5` you should return `[0,1,1,2,1,2]`.

- Follow up:

    - It is very easy to come up with a solution with run time O(n*sizeof(integer)).
    But can you do it in linear time O(n) /possibly in a single pass?
    - Space complexity should be O(n).
    - Can you do it like a **boss**? Do it without using any *builtin* function
    like `__builtin_popcount` in c++ or in any other language.

"""


def count_bits(num):
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]

    l = [0, 1]
    offset = 1

    for i in range(2, num + 1):
        if offset * 2 == i:
            offset *= 2

        l.append(1 + l[i - offset])

    return l


def count_ones(num):
    count = 0

    while num:
        count += 1

        num &= num - 1
        # print(count, num)
    return count


print(count_bits(10))
count_ones(100)
