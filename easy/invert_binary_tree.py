# Definition for a binary tree node.
from typing import Optional

""""""""""""""""""""""""""""
------------------------------------
OPTIMAL: DFS (Preorder or Postorder)
------------------------------------
TC: O(n)
SC: O(1)

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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @link - https://neetcode.io/problems/invert-a-binary-tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.revise(root)

    def revise(self, root):
        if not root:
            return None

        left = self.revise(root.left)
        right = self.revise(root.right)

        root.left = right
        root.right = left

        return root