from typing import List

# @link - https://neetcode.io/problems/target-sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.solve(nums, target)

    def solve(self, nums, target):
        n = len(nums)
        dp = [[-1 for _ in range(3000)] for _ in range(n)]
        return self.dp(nums, target, 0, dp)

    def dp(self, nums, target, i, dp):
        if i >= len(nums) and target == 0:
            return 1

        if i >= len(nums):
            return 0

        if dp[i][target + 1000] != -1:
            return dp[i][target + 1000]

        plus = self.dp(nums, target - nums[i], i + 1, dp)
        minus = self.dp(nums, target + nums[i], i + 1, dp)

        dp[i][target + 1000] = plus + minus
        return dp[i][target + 1000]