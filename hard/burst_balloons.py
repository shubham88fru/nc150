from typing import List

# @link - https://neetcode.io/problems/burst-balloons
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.solve(nums)

    def solve(self, nums):
        n = len(nums)
        padded = [0] * (n + 2)
        padded[0] = 1
        padded[n + 1] = 1

        dp = [[-1 for _ in range(n + 3)] for _ in range(n + 3)]
        for i in range(n):
            padded[i + 1] = nums[i]

        return self.top_down(padded, 1, n, dp)

    def top_down(self, padded, i, j, dp):
        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        mx = -99999999999
        for idx in range(i, j + 1):
            curr = padded[i - 1] * padded[idx] * padded[j + 1] + self.top_down(padded, i, idx - 1, dp) + self.top_down(
                padded, idx + 1, j, dp)
            mx = max(mx, curr)

        dp[i][j] = mx
        return mx