# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


# @link - https://neetcode.io/problems/balanced-binary-tree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]

    def dfs(self, root):
        if root is None:
            return (0, True)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return 1 + max(left[0], right[0]), ((abs(left[0] - right[0]) <= 1) and left[1] and right[1])
