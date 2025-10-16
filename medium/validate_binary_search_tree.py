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

---------------------------------------------
BRUTE: For each node check its left and right
---------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @link - https://neetcode.io/problems/valid-binary-search-tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -5000, 5000)

    def validate(self, root, mn, mx):
        if root is None:
            return True

        if root.val <= mn:
            return False

        if root.val >= mx:
            return False

        left = self.validate(root.left, mn, root.val)
        right = self.validate(root.right, root.val, mx)

        return left and right