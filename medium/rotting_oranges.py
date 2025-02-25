from collections import deque
from typing import List

# @link - https://neetcode.io/problems/rotting-fruit
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.solve(grid)

    def solve(self, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        empty = True
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    q.append([i, j, 0])
                    empty = False
                elif grid[i][j] == 1:
                    grid[i][j] = 1000
                    empty = False

        if empty:
            return 0

        self.bfs(grid, q)

        mx = -10000
        for i in range(0, m):
            for j in range(0, n):
                mx = max(mx, grid[i][j])

        return mx if mx != 1000 else -1


    def bfs(self, grid, q):
        m = len(grid)
        n = len(grid[0])

        dirs = [[0,1], [0,-1], [1, 0], [-1,0]]
        while len(q) > 0:
            node = q.popleft()
            i = node[0]
            j = node[1]
            dist = node[2]

            for i_ in range(0, 4):
                next_i = i + dirs[i_][0]
                next_j = j + dirs[i_][1]

                if next_i<0 or next_i>=m or next_j<0 or next_j>=n or grid[next_i][next_j] == 0:
                    continue

                if grid[next_i][next_j] > dist + 1:
                    grid[next_i][next_j] = dist + 1
                    q.append([next_i, next_j, dist+1])