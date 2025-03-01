from typing import List

# @link - https://neetcode.io/problems/jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.solve(nums)

    def solve(self, nums):
        n = len(nums)

        l = 0
        r = 0
        jumps = 0
        while r < n - 1:  # careful
            max_dist = 0
            while l <= r:
                max_dist = max(max_dist, l + nums[l])
                l += 1
            r = max_dist
            jumps += 1

        return jumps
