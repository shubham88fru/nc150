from typing import List

# @link - https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices)

    def solve(self, prices):
        n = len(prices)
        dp = [[-1 for _ in range(3)] for _ in range(n+1)]

        return self.dp(prices, 0, 1, dp)

    def dp(self, prices, i, can_buy, dp):
        if i >= len(prices):
            return 0

        if dp[i][can_buy] != -1:
            return dp[i][can_buy]

        buy = 0
        sell = 0
        if can_buy == 1:
            buy = -prices[i] + self.dp(prices, i+1, 0, dp)
        else:
            sell = prices[i] + self.dp(prices, i+2, 1, dp)

        idle = self.dp(prices, i+1, can_buy, dp)

        dp[i][can_buy] = max(buy, max(sell, idle))
        return dp[i][can_buy]