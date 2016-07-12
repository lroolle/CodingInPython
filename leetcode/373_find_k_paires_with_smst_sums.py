"""LeetCode 373. Find K pairs with smallest sums

> You are given two integer arrays nums1 and nums2 sorted in ascending order
and an integer k.

Define a pair (u, v) which consists of one element from the first array and
one element from the second array.

Find the k pairs (u1, v1),(u2, v2) ...(uk, vk) with the smallest sums.

- Example 1:
Given nums1 = [1, 7, 11], nums2 = [2, 4, 6],  k = 3

Return: [1, 2],[1, 4],[1, 6]

The first 3 pairs are returned from the sequence:
[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]

- Example 2:
Given nums1 = [1, 1, 2], nums2 = [1, 2, 3],  k = 2

Return: [1, 1], [1, 1]

The first 2 pairs are returned from the sequence:
[1, 1], [1, 1], [1, 2], [2, 1], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]

- Example 3:
Given nums1 = [1, 2], nums2 = [3],  k = 3

Return: [1, 3], [2, 3]

All possible pairs are returned from the sequence:
[1, 3], [2, 3]
"""

import heapq


def find_smallest_sums1(nums1, nums2, k):
    res = list()
    for m in nums1:
        for n in nums2:
            res.append([m, n])
    res = sorted(res, key=lambda x: sum(x))
    return res[:k]


def k_smallest_pairs2(nums1, nums2, k, heap=[]):
    for n1 in nums1:
        for n2 in nums2:
            if len(heap) < k:
                heapq.heappush(heap, (-n1 - n2, [n1, n2]))
            else:
                if heap and -heap[0][0] > n1 + n2:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                else:
                    break
    return [heapq.heappop(heap)[1] for _ in range(k) if heap]


nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 3

res = k_smallest_pairs1(nums1, nums2, k)
print(res)
print(k_smallest_pairs2(nums1, nums2, k))
