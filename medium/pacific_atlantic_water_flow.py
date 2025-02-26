from typing import List

# @link - https://neetcode.io/problems/pacific-atlantic-water-flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return self.solve(heights)

    # Following is my naive approach.
    # I'm sure there's a clever approach
    # but don't wanna (possibly) waste many
    # trying to come up with an optimal approach
    # myself. Need to check for optional soln
    # on YT.
    def solve(self, heights):
        m = len(heights)
        n = len(heights[0])

        ans = []
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == n - 1:
                    ans.append([i, j])
                elif i == m - 1 and j == 0:
                    ans.append([i, j])
                else:
                    visited = [[0 for _ in range(n)] for _ in range(m)]
                    oceans = [0, 0]
                    self.dfs(heights, visited, oceans, i, j, 5000)
                    if oceans[0] == 1 and oceans[1] == 1:
                        ans.append([i, j])

        return ans

    def dfs(self, heights, visited, oceans, i, j, prev):
        if i >= len(heights) or j >= len(heights[0]):
            oceans[1] = 1
            return

        if i < 0 or j < 0:
            oceans[0] = 1
            return

        if heights[i][j] > prev:
            return

        if visited[i][j] == 1:
            return

        visited[i][j] = 1

        self.dfs(heights, visited, oceans, i, j + 1, heights[i][j])
        self.dfs(heights, visited, oceans, i, j - 1, heights[i][j])
        self.dfs(heights, visited, oceans, i - 1, j, heights[i][j])
        self.dfs(heights, visited, oceans, i + 1, j, heights[i][j])