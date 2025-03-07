from typing import List

# @link - https://neetcode.io/problems/coin-change-ii
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.solve(amount, coins)

    def solve(self, amount, coins):
        n = len(coins)

        dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
        return self.dp(coins, amount, 0, dp)

    def dp(self, coins, amount, i, dp):
        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if i >= len(coins):
            return 0

        if dp[i][amount] != -1:
            return dp[i][amount]

        pick = self.dp(coins, amount - coins[i], i, dp)
        skip = self.dp(coins, amount, i + 1, dp)

        dp[i][amount] = pick + skip

        return dp[i][amount]