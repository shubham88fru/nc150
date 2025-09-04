# Definition for a binary tree node.
""""""""""""""""""""""""""""
------------
OPTIMAL: DFS
------------
TC: O(n)
SC: O(1)

---------------------
BETTER: BFS (2 queue)
---------------------
TC: O(n)
SC: O(1)

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


# @link - https://neetcode.io/problems/same-binary-tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)

    def dfs(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left = self.dfs(p.left, q.left)
        right = self.dfs(p.right, q.right)

        return left and right
