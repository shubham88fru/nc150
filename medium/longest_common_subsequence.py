# @link - https://neetcode.io/problems/longest-common-subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1, text2)

    def solve(self, text1, text2):
        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(text1, text2, 0, 0, dp)

    def dp(self, s1, s2, i, j, dp):
        if i >= len(s1):
            return 0

        if j >= len(s2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        same = 0
        moveI = 0
        moveJ = 0

        if s1[i] == s2[j]:
            same = 1 + self.dp(s1, s2, i+1, j+1, dp)
        else:
            moveI = self.dp(s1, s2, i+1, j, dp)
            moveJ = self.dp(s1, s2, i, j+1, dp)

        dp[i][j] = max(same, max(moveI, moveJ))
        return dp[i][j]