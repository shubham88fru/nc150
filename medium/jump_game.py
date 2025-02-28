from typing import List

# @link - https://neetcode.io/problems/jump-game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.solve(nums)

    def solve(self, nums):
        n = len(nums)
        target = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] >= target - i:
                target = i

        return target <= 0