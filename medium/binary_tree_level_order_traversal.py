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
        return self.bfs(root)

    def bfs(self, root):
        ans = []
        if root is None:
            return ans

        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            sub = []

            while sz > 0:
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                sub.append(node.val)
                sz -= 1

            ans.append(sub)

        return ans