from typing import List

# @link - https://neetcode.io/problems/buy-and-sell-crypto
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        n = len(prices)

        mx = 0
        while j < n:
            if prices[j] >= prices[i]:
                mx = max(mx, prices[j] - prices[i])
                j += 1
            else:
                i = j

        return mx
