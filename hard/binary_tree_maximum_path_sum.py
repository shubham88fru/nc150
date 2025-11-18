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

# @link - https://neetcode.io/problems/binary-tree-maximum-path-sum
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return self.solve(root)
        return self.revise(root)
    def revise(self, root):
        return self.dfs(root)[1]

    # My soln that doesn't use
    # a global max variable.
    # Might be a bit difficult
    # to get right in the first go.
    def dfs(self, root):
        if not root:
            return -99999999, -99999999

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        mx = max(l[0] + root.val, r[0] + root.val, root.val)
        return mx, max(mx, l[1], r[1], l[0] + r[0] + root.val)

    def solve(self, root):
        maxi = [-99999999999]
        self.dfs(root, maxi)
        return maxi[0]

    def dfs(self, root, maxi):
        if root is None:
            return 0

        left = max(0, self.dfs(root.left, maxi))
        right = max(0, self.dfs(root.right, maxi))

        maxi[0] = max(maxi[0], root.val + left + right)
        return root.val + max(left, right)