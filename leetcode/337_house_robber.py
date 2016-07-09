"""LeetCode 337. House Robber III

> The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root".
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this
place forms a binary tree". It will automatically contact the police
if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob
tonight without alerting the police.

- Example 1:

     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

- Example 2:

     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """DFS

    The dfs function returns an array, the first element means the maximum if
    we include the value of the current node,and the second element means the
    maximum if we  exclude the value of the current node. So in the return
    statement, as the first element, we include the value of the current
    node, and we should exclude the left and right children, so we add the
    second element from the result of left and right children. The second
    element has 4 conditions, we can include the left child and include the
    right child, include the left child and exclude the right child...,
    so we return the maximum of them.
    """

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return [0, 0]
            left, right = dfs(node.left), dfs(node.right)
            return [node.val + left[1] + right[1], max(
                    [left[0] + right[0], left[0] + right[1], left[1] + right[0],
                     left[1] + right[1]])]

        return max(dfs(root))


class Solution2(object):
    """记忆化搜索（DFS + Memorization）

    记当前房间为root，如果偷窃当前房间，则其左右孩子left和right均不能偷窃；\
    而其4个孙子节点（ll，lr，rl，rr）不受影响。

    因此最大收益为：

        maxBenifit = max(rob(left) + rob(right),
                        root.val + rob(ll) +
                        rob(lr) + rob(rl) + rob(rr))

    使用字典valMap记录每一个访问过的节点，可以避免重复运算。

    """

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        valMap = dict()

        def solve(root, path):
            if root is None: return 0
            if path not in valMap:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:  ll, lr = left.left, left.right
                if right: rl, rr = right.left, right.right
                passup = solve(left, path + 'l') + solve(right, path + 'r')
                grabit = root.val + solve(ll, path + 'll') + solve(lr,
                                                                   path + 'lr') + solve(
                        rl, path + 'rl') + solve(rr, path + 'rr')
                valMap[path] = max(passup, grabit)

            return valMap[path]

        return solve(root, '')
