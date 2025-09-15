""""""""""""""""""""""""""""
----------------------------------
OPTIMAL: Smart DFS considering BST
----------------------------------
TC: O(log(n))
SC: O(1)

------------------------------------
BETTER: 
------------------------------------
TC:
SC:

----------------
BRUTE: Plain DFS
----------------
TC: O(n)
SC: O(1)

"""""""""""""""""""""""""""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @link - https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # return self.revise(root, p, q)
        return self.revise2(root, p, q)

    # ideal soln.
    def revise2(self, root, p, q):
        ans = root
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

            ans = curr

        return ans

    # okayish soln.
    def revise(self, root, p, q):
        return self.dfs(root, p, q)[0]

    def dfs(self, root, p, q):
        if not root:
            return None, False

        if root.val == p.val or root.val == q.val:
            return root, True

        l = None, False
        if p.val <= root.val or q.val <= root.val:
            l = self.dfs(root.left, p, q)

        r = None, False
        if p.val >= root.val or q.val >= root.val:
            r = self.dfs(root.right, p, q)

        if l[1] and r[1]:
            return root, True

        if l[1]:
            return l

        return r