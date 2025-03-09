import heapq
from typing import List

# @link - https://neetcode.io/problems/min-cost-to-connect-points
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.solve(points)

    # This is some nasty, hacky soln based on prims
    # algorithm for min spanning tree. I think (could be wrong though)
    # the best way to solve this problem is through DSU. Check strvr and
    # others for optimal soln.
    def solve(self, points):
        graph = self.get_graph(points)
        print(graph)
        return self.prims(graph, points[0])

    def prims(self, graph, start):
        pq = []
        heapq.heapify(pq)

        heapq.heappush(pq, (0, start[0], start[1]))

        costs = {}
        min_cost = 0
        while len(pq) > 0:
            curr = heapq.heappop(pq)
            if (curr[1], curr[2]) in costs:
                continue

            costs[(curr[1], curr[2])] = curr[0]
            min_cost += curr[0]

            ngs = graph.get((curr[1], curr[2]), [])
            for ng in ngs:
                x, y, wt = ng
                heapq.heappush(pq, (wt, x, y))

        return min_cost

    def get_graph(self, points):
        graph = {}

        for i in range(0, len(points)):
            tpl1 = (points[i][0], points[i][1])
            for j in range(0, len(points)):
                if i == j:
                    continue

                wt = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                tpl2 = (points[j][0], points[j][1], wt)
                # graph[tpl1] = graph.get(tpl1, []).append(tpl2)
                # graph.setdefault(tpl1, []).append(tpl2)
                if tpl1 not in graph:
                    graph[tpl1] = []

                graph.get(tpl1).append(tpl2)

        return graph