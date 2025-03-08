# @link - https://neetcode.io/problems/edit-distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.solve(word1, word2)

    def solve(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)

        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.dp(word1, word2, 0, 0, dp)

    def dp(self, word1, word2, i, j, dp):
        if i >= len(word1):
            return len(word2) - j

        if j >= len(word2):
            return len(word1) - i

        if dp[i][j] != -1:
            return dp[i][j]

        ch1 = word1[i]
        ch2 = word2[j]

        if ch1 == ch2:
            return self.dp(word1, word2, i + 1, j + 1, dp)

        insert = 1 + self.dp(word1, word2, i, j + 1, dp)
        replace = 1 + self.dp(word1, word2, i + 1, j + 1, dp)
        delete = 1 + self.dp(word1, word2, i + 1, j, dp)

        return min(insert, replace, delete)