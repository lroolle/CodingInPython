"""Two Sum

# Two Sum
> Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

> You may assume that each input would have exactly one solution.

- Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    UPDATE (2016/2/13):
    The return format had been changed to zero-based indices.
    Please read the above updated description carefully.

"""


def two_sum(a, target):
    off = 0
    while off < len(a):
        for i in range(off + 1, len(a)):
            if a[off] + a[i] == target:
                return [off, i]
        off += 1


def two_sum2(a, target):
        map = dict()
        size = len(a)
        for x in range(size):
            map[a[x]] = x
        for x in range(size):
            idx1 = x
            idx2 = map.get(target - a[x])
            if idx2:
                return [idx1, idx2]


print(two_sum([0, 1, 2, 3], 4))
print(two_sum2([0, 1, 2, 3], 4))
