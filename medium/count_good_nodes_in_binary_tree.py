# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @link - https://neetcode.io/problems/count-good-nodes-in-binary-tree
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.solve(root)

    def solve(self, root):
        mx = -500
        ans = [0]
        self.dfs(root, mx, ans)
        return ans[0]

    def dfs(self, root, mx, ans):
        if root is None:
            return


        if root.val >= mx:
            ans[0] += 1

        self.dfs(root.left, max(mx, root.val), ans)
        self.dfs(root.right, max(mx, root.val), ans)