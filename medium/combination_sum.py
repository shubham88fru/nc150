from typing import List

# @link - https://neetcode.io/problems/combination-target-sum
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.solve(nums, target)

    def solve(self, nums, target):
        ans = []
        self.backtrack(nums, target, 0, ans, [])
        return ans

    def backtrack(self, nums, target, i, ans, curr):
        if target == 0:
            ans.append(list(curr))
            return

        if i >= len(nums):
            return

        if target - nums[i] >= 0:
            curr.append(nums[i])
            self.backtrack(nums, target-nums[i], i, ans, curr)
            curr.pop()

        self.backtrack(nums, target, i+1, ans, curr)