# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @link - https://neetcode.io/problems/binary-tree-maximum-path-sum
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)

    def solve(self, root):
        maxi = [-99999999999]
        self.dfs(root, maxi)
        return maxi[0]

    def dfs(self, root, maxi):
        if root is None:
            return 0

        left = max(0, self.dfs(root.left, maxi))
        right = max(0, self.dfs(root.right, maxi))

        maxi[0] = max(maxi[0], root.val + left + right)
        return root.val + max(left, right)