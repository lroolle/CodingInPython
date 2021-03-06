"""LeetCode 349. Intersection of Two Arrays

> Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
- Each element in the result must be unique.
- The result can be in any order.

"""


def intersection_arr(a1, a2):
    return list(set(a1) & set(a2))


print(intersection_arr([1, 2, 2, 1], [2, 2]))
