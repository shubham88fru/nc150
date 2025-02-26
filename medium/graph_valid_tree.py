from typing import List

# @link - https://neetcode.io/problems/valid-tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.solve(n, edges)

    def solve(self, n, edges):
        # A tree is a graph with the following conditions:
        # 1. Directed (in this q doesn't matter, though)
        # 2. No cycles.
        # 3. Edges equal to nodes-1

        # Therefore, if a graph has less than n-1 edges,
        # means it is disconnected, and if it has more than
        # n-1 edges, it must mean that the graph has cycles.
        # Both these cases can never lead to a valid tree.
        if len(edges) != n - 1:
            return False

        # At this point it is ensured that the graph has
        # n-1 edges. However, that is not enough. A graph
        # maybe very well have n-1 edges but still not be
        # a valid tree. This can happen when the graph has
        # cycle and is disconnected. e.g. -
        # 1---3
        #  \ /  4
        #   2
        # n = 4 and e = 3 but still not a valid tree.

        # So, having ensured that the graph has n-1 edges,
        # all we need to confirm is that we can visit
        # all the nodes starting from any node.

        graph = self.get_graph(n, edges)
        visited = set()
        self.dfs(graph, 0, visited)

        return len(visited) == n

    def dfs(self, graph, curr, visited):
        if curr in visited:
            return

        visited.add(curr)
        ngs = graph[curr]
        for i in range(0, len(ngs)):
            self.dfs(graph, ngs[i], visited)

    def get_graph(self, n, edges):
        graph = []
        for i in range(0, n):
            graph.append([])

        for i in range(0, len(edges)):
            u = edges[i][0]
            v = edges[i][1]

            graph[u].append(v)
            graph[v].append(u)

        return graph