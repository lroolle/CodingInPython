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
