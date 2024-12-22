# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @link - https://neetcode.io/problems/binary-tree-diameter
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1] - 1

    def dfs(self, root):
        if root is None:
            return 0, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return 1 + max(left[0], right[0]), max(left[1], right[1], 1 + left[0] + right[0])