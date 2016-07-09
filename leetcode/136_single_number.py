"""Single Number

> Given an array of integers, every element appears twice except for one.
Find that single one.

- Note:
    Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?

"""


def single_num(nums):
    res = 0
    for num in nums:
        res ^= num

    return res


def single_num2(nums):
    nums = sorted(nums)

    index = 0

    while index < len(nums) - 3:
        if nums[index] != nums[index + 1]:
            return nums[index]
        if nums[index] != nums[index + 3]:
            return nums[index + 3]

        index += 3

    return nums[index]


nums = [1, 1, 2, 3, 3]
print(single_num(nums))
