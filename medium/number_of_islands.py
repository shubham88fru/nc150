from typing import List

""""""""""""""""""""""""""""
---------------------------
OPTIMAL: DFS/BFS/Union Find
---------------------------
TC: O(m*n); bc each cell is visited atmost once.
SC: O(1)

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
# @link - https://neetcode.io/problems/count-number-of-islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.solve(grid)

    def solve(self, grid):
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    self.dfs(grid, visited, i, j, m, n)
        return count

    def dfs(self, grid, visited, i, j, m, n):
        if i<0 or i>=m or j<0 or j>=n or visited[i][j] == -1 or grid[i][j] == '0':
            return

        visited[i][j] = -1

        self.dfs(grid, visited, i, j+1, m, n) # right
        self.dfs(grid, visited, i+1, j, m, n) # down
        self.dfs(grid, visited, i, j-1, m, n) # left
        self.dfs(grid, visited, i-1, j, m, n) # up