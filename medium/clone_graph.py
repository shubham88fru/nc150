from collections import deque
from typing import Optional

""""""""""""""""""""""""""""
----------------
OPTIMAL: BFS/DFS
----------------
TC: O(n); n is number of nodes in graph.
SC: O(n); for map

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

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# @link - https://neetcode.io/problems/clone-graph
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.solve(node)

    def solve(self, node):
        # return self.bfs(node)
        return self.dfs(node, {})

    # Sol 1 - using dfs
    def dfs(self, node, visited):
        if node is None:
            return None

        cpy = Node(node.val)
        visited[node] = cpy
        cpy.neighbors = []
        neighbors = node.neighbors

        for i in range(0, len(neighbors)):
            if neighbors[i] not in visited:
                cpy.neighbors.append(self.dfs(neighbors[i], visited))
            else:
                cpy.neighbors.append(visited[neighbors[i]])

        return cpy

    # Sol 2 - Using bfs (uses a lot of extra space)
    def bfs(self, node):
        if node is None:
            return None

        ogQ = deque()
        ogQ.append(node)

        cpQ = deque()
        cpNode = Node(node.val)
        cpQ.append(cpNode)

        visited = {}
        visited[node] = cpNode

        while len(ogQ) > 0:
            ogNode = ogQ.popleft()
            currCpy = cpQ.popleft()
            currCpy.neighbors = []

            for i in range(0, len(ogNode.neighbors)):
                cpNg = None
                if ogNode.neighbors[i] not in visited:
                    cpNg = Node(ogNode.neighbors[i].val)
                    ogQ.append(ogNode.neighbors[i])
                    cpQ.append(cpNg)
                    visited[ogNode.neighbors[i]] = cpNg
                else:
                    cpNg = visited[ogNode.neighbors[i]]

                currCpy.neighbors.append(cpNg)

        return cpNode