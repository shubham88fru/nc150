from typing import List

# @link - https://neetcode.io/problems/redundant-connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.solve(edges)

    # 3. (Brute) Iterate the edges from back and keep
    # forming a graph without the current edge.
    # if the graph is connected and
    # doesn't have cycle, that means
    # current edge is redundant.

    # 2. Iterate the graph from the start and keep forming graph,
    # for each edge, check if u and v both
    # are are present in the graph already, if so,
    # run a dfs and see if we can reach from u to v.
    # If yes, then it mean that the current edge is
    # redundant.

    # Optimal solution using DSU
    def solve(self, edges):
        n = len(edges)

        # dsu = RawDSU(n)
        dsu = PathCompressionAndRankingDSU(n)
        for edge in edges:
            u = edge[0]
            v = edge[1]

            if dsu.find(u) == dsu.find(v):
                return edge

            dsu.union(u, v)

        return []


# Mik said that this problem can be solved using
# raw dsu also, but I don't this. Tried raw
# dsu but realized that atleast path compression is
# needed. So bassically dsu with path compresion only,
# dsu with path compression and ranking both works,
# but raw dsu doent.
class PathCompressionAndRankingDSU:
    def __init__(self, n):
        self.parents = []
        for i in range(n + 1):
            self.parents.append(i)

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        self.parents[pu] = pv
        return True