# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @link - https://neetcode.io/problems/kth-smallest-integer-in-bst
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.solve(root, k)

    def solve(self, root, k):
        kay = [k]
        return self.dfs(root, kay)

    def dfs(self, root, kay):
        if root is None:
            return -1

        left = self.dfs(root.left, kay)
        if left != -1:
            return left

        kay[0] -= 1
        if kay[0] == 0:
            return root.val

        right = self.dfs(root.right, kay)
        if right != -1:
            return right

        return -1