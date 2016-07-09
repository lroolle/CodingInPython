"""Move Zeros

> Given an array nums, write a function to move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimize the total number of operations.

"""


# Not in-place!
def move_0(nums):
    size = len(nums)
    count = 0

    for i in range(size):
        if nums[i] != 0:
            nums.append(nums[i])
            count += 1

    for j in range(size - count):
        nums.append(0)

    return nums[size:]


# In-place is Very Important!
def move_0_in_place(nums):
    size = len(nums)
    i, count = 0, 0

    while i < size - count:
        if nums[i] == 0:
            for j in range(i + 1, size - count):
                nums[j - 1] = nums[j]
            count += 1
            nums[size - 1] = 0
        i += 1


a = [0, 1, 2, 0, 3, 0]
print(a)
move_0_in_place(a)
print(a)
print(move_0(a))
