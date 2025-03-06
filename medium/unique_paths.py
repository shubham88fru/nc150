# @link - https://neetcode.io/problems/count-paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m, n)

    def solve(self, m, n):
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(m, n, 0, 0, dp, [[1, 0], [0, 1]])

    def dp(self, m, n, i, j, dp, dirs):
        if i == m - 1 and j == n - 1:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        count = 0
        for idx in range(0, len(dirs)):
            next_i = dirs[idx][0] + i
            next_j = dirs[idx][1] + j
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue

            count += self.dp(m, n, next_i, next_j, dp, dirs)

        dp[i][j] = count
        return dp[i][j]