""""""""""""""""""""""""""""
------------
OPTIMAL: BFS
------------
TC: O(n)
SC: O(n/2); queue size will be at max n/2

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
from typing import Optional, List


# @link - https://neetcode.io/problems/level-order-traversal-of-binary-tree
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.revise(root)

    def revise(self, root):
        ans = []

        if not root:
            return ans

        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            level = []
            while sz > 0:
                rt = q.popleft()
                level.append(rt.val)

                if rt.left:
                    q.append(rt.left)

                if rt.right:
                    q.append(rt.right)

                sz -= 1

            ans.append(level)

        return ans