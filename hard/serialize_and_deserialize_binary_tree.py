""""""""""""""""""""""""""""
--------------------
OPTIMAL: DFS and BFS
--------------------
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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @link - https://neetcode.io/problems/serialize-and-deserialize-binary-tree

# Following is the DFS soln.
# There's a BFS soln also which has
# same TC/SC, but it's just a different
# approach to know. My java playlist has
# that approach.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        lst = []
        self.ser(root, lst)
        return ",".join(lst)

    def ser(self, root, lst):
        if not root:
            lst.append("#")
            return

        lst.append(str(root.val))

        self.ser(root.left, lst)
        self.ser(root.right, lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        return self.deser(nodes, [0])

    def deser(self, nodes, i):
        if (nodes[i[0]] == "#"):
            i[0] += 1
            return None

        root = TreeNode(int(nodes[i[0]]))

        i[0] += 1
        root.left = self.deser(nodes, i)
        root.right = self.deser(nodes, i)

        return root
