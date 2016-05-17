def moveZeroes( nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    index = len(nums)

    count = 0

    for i in range(index):

        if nums[i] != 0:
            nums.append(nums[i])
            count += 1

    for j in range(index - count):
        nums.append(0)

    return nums

print(moveZeroes([0, 1, 2, 0, 3, 0]))
