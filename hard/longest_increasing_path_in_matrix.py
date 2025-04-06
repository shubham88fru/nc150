from typing import List

# @link - https://neetcode.io/problems/longest-increasing-path-in-matrix
class Solution:
    def __init__(self):
        self.dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    # My dp and memoization soln.
    # It aint the optimal soln i guess.
    # check bottom up online.
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return self.solve(matrix)

    def solve(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                visited = [[0 for _ in range(n)] for _ in range(m)]
                max_len = max(max_len, self.dfs(matrix, m, n, i, j, visited, memo))

        return 1 + max_len

    def dfs(self, matrix, m, n, i, j, visited, memo):
        if memo[i][j] != -1:
            return memo[i][j]

        visited[i][j] = -1;
        max_len = 0
        for di in self.dirs:
            ni = di[0] + i
            nj = di[1] + j

            if ni < 0 or ni >= m or nj < 0 or nj >= n or visited[ni][nj] == -1 or matrix[ni][nj] <= matrix[i][j]:
                continue

            max_len = max(max_len, 1 + self.dfs(matrix, m, n, ni, nj, visited, memo));

        visited[i][j] = 0;
        memo[i][j] = max_len

        return max_len