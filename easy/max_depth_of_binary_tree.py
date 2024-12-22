# Definition for a binary tree node.
from collections import deque
from typing import Optional

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

    def dfs(self, root):
        if root is None:
            return 0

        left = 1 + self.dfs(root.left)
        right = 1 + self.dfs(root.right)

        return max(left, right)

    def bfs(self, root):
        if root is None:
            return 0

        q = deque()
        q.append(root)

        depth = 0
        while len(q) != 0:
            sz = len(q)
            while sz > 0:
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                sz -= 1

            depth += 1

        return depth