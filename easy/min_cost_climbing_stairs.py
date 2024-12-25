from typing import List

# @link - https://neetcode.io/problems/min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.dfs(cost, 0, {}), self.dfs(cost, 1, {}))

    def dfs(self, cost, curr, cache):
        if curr >= len(cost):
            return 0

        if curr in cache:
            return cache[curr]

        one_j = cost[curr] + self.dfs(cost, curr + 1, cache)
        two_j = cost[curr] + self.dfs(cost, curr + 2, cache)

        cache[curr] = min(one_j, two_j)
        return cache[curr]