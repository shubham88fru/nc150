# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @link - https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.solve(preorder, inorder)

    def solve(self, preorder, inorder):
        mp = {}
        for idx, item in enumerate(inorder):
            mp[item] = idx

        pidx = [0]
        return self.construct(preorder, inorder, pidx, 0, len(inorder) - 1, mp)

    def construct(self, preorder, inorder, pidx, mini, maxi, mp):

        if mini > maxi:
            return None

        curr = preorder[pidx[0]]
        root = TreeNode(curr)

        iidx = mp[curr]
        pidx[0] += 1

        root.left = self.construct(preorder, inorder, pidx, mini, iidx - 1, mp)
        root.right = self.construct(preorder, inorder, pidx, iidx + 1, maxi, mp)

        return root