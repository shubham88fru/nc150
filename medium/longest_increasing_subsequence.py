from typing import List

# @link - https://neetcode.io/problems/longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve(nums)

    # This is certainly not a optimal soln.
    # I guess the only optimal dp soln is bottom up.
    # Redo this problem during revision at strvr.
    def solve(self, nums):
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        return self.dp(nums, dp, -1, 0)

    def dp(self, nums, dp, mini, i):
        if i >= len(nums):
            return 0

        if mini != -1 and dp[i][mini] != -1:
            return dp[i][mini]

        pick = 0
        if mini == -1 or nums[i] > nums[mini]:
            pick = 1 + self.dp(nums, dp, i, i + 1)

        notPick = self.dp(nums, dp, mini, i + 1)

        if mini != -1:
            dp[i][mini] = max(pick, notPick)

        return max(pick, notPick)