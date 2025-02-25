from typing import List

# @link - https://neetcode.io/problems/islands-and-treasure
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        return self.solve(grid)

    def solve(self, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 0:
                    q.append([i, j, 0])

        self.bfs(grid, q)

    def bfs(self, grid, q):
        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while len(q) > 0:
            node = q.popleft()
            i = node[0]
            j = node[1]
            dist = node[2]

            for i_ in range(0, len(dirs)):
                nextI = i + dirs[i_][0]
                nextJ = j + dirs[i_][1]
                if nextI < 0 or nextI >= m or nextJ < 0 or nextJ >= n or grid[nextI][nextJ] == -1 or grid[nextI][
                    nextJ] == 0:
                    continue

                if grid[nextI][nextJ] > dist + 1:
                    grid[nextI][nextJ] = dist + 1
                    q.append([nextI, nextJ, dist + 1])