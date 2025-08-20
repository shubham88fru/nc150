# Definition for a binary tree node.
from collections import deque
from typing import Optional

""""""""""""""""""""""""""""
----------------------------------------------
OPTIMAL: DFS (Recursive), DFS (Iterative), BFS
----------------------------------------------
TC: O(n)
SC: O(n)

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

# @link - https://neetcode.io/problems/depth-of-binary-tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        # return self.bfs(root)

    def dfs_iterative(self, root):
        if not root:
            return 0

        s = []
        s.append(root)
        st = set()

        h = 0
        while s:
            e = s[-1]
            st.add(e)

            if e.left and e.left not in st:
                s.append(e.left)
            elif e.right and e.right not in st:
                s.append(e.right)
            else:
                h = max(h, len(s))
                s.pop()

        return h

    def dfs(self, root):
        if not root:
            return 0

        left = 1 + self.dfs(root.left)
        right = 1 + self.dfs(root.right)

        return max(left, right)

    def bfs(self, root):
        if not root:
            return 0

        q = deque()
        q.append(root)

        h = 0
        while q:
            sz = len(q)
            while sz > 0:
                e = q.popleft()
                if e.left:
                    q.append(e.left)

                if e.right:
                    q.append(e.right)

                sz -= 1

            h += 1

        return h