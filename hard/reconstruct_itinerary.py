from typing import List

# @link - https://neetcode.io/problems/reconstruct-flight-path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: (x[0], x[1]))
        graph = {}
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)
        itinerary = []
        path = ["JFK"]
        self.dfs("JFK", graph, len(tickets), path, itinerary)
        return itinerary

    def dfs(self, current: str, graph: dict, n: int, currPath: List[str], itinerary: List[str]) -> bool:
        if len(currPath) == n + 1:
            itinerary.extend(currPath)
            return True
        if current not in graph:
            return False
        neighbors = list(graph[current])
        for i, neighbor in enumerate(neighbors):
            graph[current].remove(neighbor)
            currPath.append(neighbor)
            if self.dfs(neighbor, graph, n, currPath, itinerary):
                return True
            currPath.pop()
            graph[current].insert(i, neighbor)
        return False