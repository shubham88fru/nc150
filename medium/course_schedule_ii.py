from typing import List

# @link - https://neetcode.io/problems/course-schedule-ii
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.solve(numCourses, prerequisites)

    def solve(self, numCourses, prerequisites):
        graph = self.get_graph(numCourses, prerequisites)

        indegrees = [0] * numCourses
        for i in range(0, len(prerequisites)):
            v = prerequisites[i][0]
            u = prerequisites[i][1]
            indegrees[v] += 1

        q = deque()
        for i in range(0, len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)

        visited = [0] * numCourses
        toposort = []
        self.bfs(graph, prerequisites, q, indegrees, visited, toposort)

        return toposort if len(toposort) == numCourses else []

    def bfs(self, graph, prerequisites, q, indegrees, visited, toposort):
        if len(q) == 0:
            return

        while len(q) > 0:
            node = q.popleft()

            if visited[node] == -1:
                continue

            visited[node] = -1
            toposort.append(node)

            ng = graph[node]

            for i in range(0, len(ng)):
                indegrees[ng[i]] -= 1
                if indegrees[ng[i]] == 0:
                    q.append(ng[i])

    def get_graph(self, numCourses, prerequisites):
        graph = []
        for i in range(0, numCourses):
            graph.append([])

        for i in range(0, len(prerequisites)):
            v = prerequisites[i][0]
            u = prerequisites[i][1]

            graph[u].append(v)

        return graph
