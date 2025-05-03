from typing import List

""""""""""""""""""""""""""""
------------------------------------
OPTIMAL: sliding window/two pointers
------------------------------------
TC: O(n)
SC: O(1)

-------------------
BETTER: Top down dp
-------------------
TC: O(n)
SC: O(n)

---------------------------------------------------------------
BRUTE: For each day, find the next higher day we can sell stock
---------------------------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/buy-and-sell-crypto
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.solve(prices)
        return self.revise(prices)

    def solve(self, prices):
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

    def revise(self, prices):
        n = len(prices)
        mini = prices[0]
        maxProfit = 0
        for i in range(1, n):
            if prices[i] < mini:
                mini = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - mini)

        return maxProfit
