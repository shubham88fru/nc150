from collections import deque
from typing import List

# @link - https://neetcode.io/problems/cheapest-flight-path
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    return self.solve(n, flights, src, dst, k)


def solve(self, n, flights, src, dst, k):
    graph = self.get_graph(flights, n)

    return self.bfs(graph, src, dst, k, n)


def bfs(self, graph, src, dst, k, n):
    q = deque()
    q.append([src, 0])

    costs = [999999999] * n
    costs[src] = 0

    stops = 0
    while len(q) > 0 and stops <= k:
        sz = len(q)

        while sz > 0:
            curr = q.popleft()
            ngs = graph[curr[0]]
            for ng in ngs:
                if curr[1] + ng[1] < costs[ng[0]]:
                    costs[ng[0]] = curr[1] + ng[1]
                    q.append([ng[0], costs[ng[0]]])
            sz -= 1
        stops += 1

    return -1 if costs[dst] == 999999999 else costs[dst]


def get_graph(self, flights, n):
    graph = [[] for _ in range(n)]

    for flight in flights:
        u = flight[0]
        v = flight[1]
        wt = flight[2]

        graph[u].append([v, wt])

    return graph