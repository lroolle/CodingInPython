"""LeetCode 347. Top K Frequent Elements

> Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


def top_k(nums, k):
    d = {x: 0 for x in set(nums)}

    for x in nums:
        d[x] += 1

    res = sorted(d, key=d.get, reverse=True)

    return res[:k]


print(top_k([1, 1, 1, 2, 2, 3], 3))
