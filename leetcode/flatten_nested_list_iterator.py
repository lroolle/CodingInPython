"""LeetCode 341. Flatten Nested List Iterator

> Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may
also be integers or other lists.

- Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].

- Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order
of elements returned by next should be: [1,4,6].

"""


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
