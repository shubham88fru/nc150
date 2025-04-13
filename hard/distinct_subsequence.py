# @link - https://neetcode.io/problems/count-subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(s, t)

    def solve(self, s, t):
        m = len(s)
        n = len(t)

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(s, t, m, n, 0, 0, memo)

    def dp(self, s, t, m, n, i, j, memo):
        if j >= n:
            return 1

        if i >= m:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        ch1 = s[i]
        ch2 = t[j]

        pick = 0
        notPick = 0
        if ch1 == ch2:
            pick += self.dp(s, t, m, n, i + 1, j + 1, memo)

        notPick += self.dp(s, t, m, n, i + 1, j, memo)

        memo[i][j] = pick + notPick

        return memo[i][j]