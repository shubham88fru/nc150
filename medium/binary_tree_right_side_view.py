""""""""""""""""""""""""""""
----------------
OPTIMAL: DFS/BFS
----------------
TC: O(n)
SC: O(1)

-------------------------------
BETTER: Suboptimal DFS with set
-------------------------------
TC: O(n)
SC: O(levels); levels is the height of the tree

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @link - https://neetcode.io/problems/binary-tree-right-side-view
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return self.bfs(root)

        ans = []

        # self.dfs_subopt(root, set(), 0, ans)
        self.dfs_optimal(root, ans, 0)

        return ans

    def dfs_optimal(self, root, ans, lvl):
        if not root:
            return None

        if len(ans) == lvl:
            ans.append(root.val)

        self.dfs_optimal(root.right, ans, lvl + 1)
        self.dfs_optimal(root.left, ans, lvl + 1)

    def dfs_subopt(self, root, lvls, lvl, ans):
        if not root:
            return None

        if lvl not in lvls:
            lvls.add(lvl)
            ans.append(root.val)

        self.dfs_subopt(root.right, lvls, lvl + 1, ans)
        self.dfs_subopt(root.left, lvls, lvl + 1, ans)

    def bfs(self, root):
        if not root:
            return []

        ans = []
        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            while sz > 0:
                node = q.popleft()
                if sz == 1:
                    ans.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                sz -= 1

        return ans