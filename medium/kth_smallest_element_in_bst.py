""""""""""""""""""""""""""""
-----------------------------------------------------
OPTIMAL: Recursive/Iterative DFS and Morris traversal
-----------------------------------------------------
TC: O(n)
SC: O(1)

-----------------------------------
BETTER: 
-----------------------------------
TC:
SC:

------------------------------------------
BRUTE: Put in array and then iterate array
------------------------------------------
TC: O(n)
SC: O(n)

"""""""""""""""""""""""""""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @link - https://neetcode.io/problems/kth-smallest-integer-in-bst
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.solve(root, k)

    def solve(self, root, k):
        kay = [k]
        return self.dfs(root, kay)

    def dfs(self, root, kay):
        if root is None:
            return -1

        left = self.dfs(root.left, kay)
        if left != -1:
            return left

        kay[0] -= 1
        if kay[0] == 0:
            return root.val

        right = self.dfs(root.right, kay)
        if right != -1:
            return right

        return -1

    # My iterative inorder traversal.
    # Nc showed a slightly cleaner
    # iterative code.
    def iterative(self, root, k):
        stack = []
        stack.append(root)

        while stack:

            while stack[-1].left:
                stack.append(stack[-1].left)

            while stack:
                top = stack.pop()
                k -= 1
                if k == 0:
                    return top.val

                if top.right:
                    stack.append(top.right)
                    break
        return -1