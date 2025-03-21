# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# @link - https://neetcode.io/problems/serialize-and-deserialize-binary-tree
class Codec:
    i = 0

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        enc = [""]
        self.ser(root, enc)
        return enc[0]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        return self.des(data)

    def ser(self, root, enc):
        if root is None:
            enc[0] += "$"
            return

        enc[0] += str(root.val) + "#"
        self.ser(root.left, enc)
        self.ser(root.right, enc)

    def des(self, data):
        if self.i >= len(data):
            return None

        ch = data[self.i]
        if ch == "$":
            self.i += 1
            return None

        sub = ""
        while (self.i < len(data) and data[self.i] != "#"):
            sub += data[self.i]
            self.i += 1

        node = TreeNode(int(sub))

        self.i += 1
        node.left = self.des(data)
        node.right = self.des(data)

        return node