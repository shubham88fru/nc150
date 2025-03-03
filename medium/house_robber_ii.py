from typing import List

# @link - https://neetcode.io/problems/house-robber-ii
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums)

    def solve(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(
            self.dp(nums, 0, n-2, [-1]*n),
            self.dp(nums, 1, n-1, [-1]*n)
        )

    def dp(self, nums, i, limit, memo):
        if i > limit:
            return 0

        if memo[i] != -1:
            return memo[i]

        rob = nums[i] + self.dp(nums, i+2, limit, memo)
        dontRob = self.dp(nums, i+1, limit, memo)
        memo[i] = max(rob, dontRob)
        return memo[i]