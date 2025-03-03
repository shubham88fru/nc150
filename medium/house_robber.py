from typing import List

# @link - https://neetcode.io/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums)

    # Top-down approach.
    # check yt/nc if bottom-up is
    # necessary.
    def solve(self, nums):
        dp = [-1] * len(nums)
        return self.dp(nums, 0, dp)

    def dp(self, nums, i, dp):
        if i >= len(nums):
            return 0

        if dp[i] != -1:
            return dp[i]

        rob = nums[i] + self.dp(nums, i + 2, dp)
        dont_rob = self.dp(nums, i + 1, dp)

        dp[i] = max(rob, dont_rob)
        return dp[i]