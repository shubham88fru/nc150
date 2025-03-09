import heapq
from typing import List

# @link - https://neetcode.io/problems/network-delay-time
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return self.solve(times, n, k)

    def solve(self, times, n, k):
        graph = self.build_graph(times, n)

        min_costs = [99999999] * (n + 1)
        min_costs[k] = 0
        self.dijkstra(graph, min_costs, n, k)

        mx = max(min_costs[1:])
        return -1 if mx == 99999999 else mx

    def dijkstra(self, graph, min_costs, n, k):
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, [k, 0])

        while len(min_heap) > 0:
            curr = heapq.heappop(min_heap)
            ngs = graph[curr[0]]
            for ng in ngs:
                nxt = ng[0]
                nxt_wt = ng[1]

                if min_costs[curr[0]] + nxt_wt < min_costs[nxt]:
                    min_costs[nxt] = min_costs[curr[0]] + nxt_wt
                    heapq.heappush(min_heap, ng)

    def build_graph(self, times, n):
        graph = [[] for _ in range(n + 1)]

        for i in range(0, len(times)):
            u = times[i][0]
            v = times[i][1]
            w = times[i][2]

            graph[u].append([v, w])

        return graph