from typing import List

# @link - https://neetcode.io/problems/count-connected-components
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return self.solve(n, edges)

    # I'm really sure if this is the optimal approach for
    # this problem (more likely not). Check online solutions
    # for the optimal appraoch.
    def solve(self, n, edges):
        graph = self.get_graph(n, edges)

        comp = 0
        visited = [0] * n
        for i in range(0, n):
            if visited[i] == 0:
                comp += 1
                self.dfs(graph, edges, visited, i)

        return comp

    def dfs(self, graph, edges, visited, curr):
        if visited[curr] == -1:
            return

        visited[curr] = -1

        ngs = graph[curr]
        for i in range(0, len(ngs)):
            self.dfs(graph, edges, visited, ngs[i])

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