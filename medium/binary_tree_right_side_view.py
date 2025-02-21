# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# @link - https://neetcode.io/problems/binary-tree-right-side-view
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.solve(root)

    def solve(self, root):
        lvls = set()
        ans = []
        self.dfs(root, ans, 0, lvls)
        return ans

    def dfs(self, root, ans, lvl, lvls):
        if root is None:
            return

        if lvl not in lvls:
            lvls.add(lvl)
            ans.append(root.val)

        self.dfs(root.right, ans, lvl+1, lvls)
        self.dfs(root.left, ans, lvl+1, lvls)