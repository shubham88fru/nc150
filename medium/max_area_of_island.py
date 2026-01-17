from typing import List

""""""""""""""""""""""""""""
---------------------------
OPTIMAL: DFS/BFS/Union Find
---------------------------
TC: O(m*n); visiting each cell atmost once.
SC: O(m*n)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/max-area-of-island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.solve(grid)

    def solve(self, grid):
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        maxArea = 0
        for i in range(0, m):
            for j in range(0, n):
                area = [0]
                if grid[i][j] == 1 and visited[i][j] == 0:
                    self.dfs(grid, visited, i, j, m, n, area)
                    maxArea = max(maxArea, area[0])

        return maxArea

    def dfs(self, grid, visited, i, j, m, n, area):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == -1 or grid[i][j] == 0:
            return

        visited[i][j] = -1
        area[0] += 1
        self.dfs(grid, visited, i, j + 1, m, n, area)  # right
        self.dfs(grid, visited, i + 1, j, m, n, area)  # down
        self.dfs(grid, visited, i, j - 1, m, n, area)  # left
        self.dfs(grid, visited, i - 1, j, m, n, area)  # up