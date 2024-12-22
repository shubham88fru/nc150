# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @link - https://neetcode.io/problems/invert-a-binary-tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root

    def dfs(self, root):
        if root is None:
            return

        self.dfs(root.left)
        self.dfs(root.right)

        temp = root.right
        root.right = root.left
        root.left = temp

        return