# Definition for a binary tree node.
""""""""""""""""""""""""""""
------------
OPTIMAL: DFS
------------
TC: O(n)
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

---------------------------------------------------------
BRUTE: At each node run dfs for left and right (check nc)
---------------------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""
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

    def revise(self, root):
        if not root:
            return 0, True

        left = self.revise(root.left)
        right = self.revise(root.right)

        diff = abs(left[0] - right[0])
        if diff <= 1 and left[1] and right[1]:
            return 1 + max(left[0], right[0]), True

        return -1, False
