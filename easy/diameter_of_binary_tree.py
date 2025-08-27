""""""""""""""""""""""""""""
------------
OPTIMAL: DFS
------------
TC: O(n)
SC: O(1), only recursive stack space.

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
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
        return self.revise(root)

    def revise(self, root):
        return self.diam(root)[1]

    def diam(self, root):
        if not root:
            return [0, 0]

        left = self.diam(root.left)
        right = self.diam(root.right)

        return [1 + max(left[0], right[0]), max(max(left[1], right[1]), left[0] + right[0])]