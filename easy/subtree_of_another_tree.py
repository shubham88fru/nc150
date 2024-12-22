# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


# @link - https://neetcode.io/problems/subtree-of-a-binary-tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)

    def dfs(self, root, subRoot):
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val == subRoot.val and self.sameTree(root, subRoot):
            return True

        left = self.dfs(root.left, subRoot)
        if left:
            return True

        right = self.dfs(root.right, subRoot)
        if right:
            return True

        return left or right

    def sameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right