# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @link - https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.sol2(root, p, q)

    # Simple DFS, doesn't use the fact that the
    # given tree is a BST.
    # In an interview its almost
    # certain that there will be a
    # followup.
    def sol2(self, root, p, q):
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left

        return right