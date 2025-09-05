# Definition for a binary tree node.
""""""""""""""""""""""""""""
------------
OPTIMAL: DFS
------------
TC: O(s*t); where s is nodes in root and t is the number of nodes in subroot
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.revise(root, subRoot)

    def revise(self, root, subRoot):
        return self.dfs(root, subRoot)

    def dfs_revise(self, root, subRoot):
        if not root:
            return subRoot == None

        same = False
        if root.val == subRoot.val:
            same = self.same_tree(root, subRoot)

        if same:
            return True

        left = self.dfs_revise(root.left, subRoot)
        right = self.dfs_revise(root.right, subRoot)

        return left or right

    def same_tree(self, r1, r2):
        if not r1 and not r2:
            return True

        if not r1:
            return False

        if not r2:
            return False

        if r1.val != r2.val:
            return False

        left = self.same_tree(r1.left, r2.left)
        right = self.same_tree(r1.right, r2.right)

        return left and right