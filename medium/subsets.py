from typing import List

# @link - https://neetcode.io/problems/subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.solve(nums)

    def solve(self, nums):
        ans = []
        self.backtrack(nums, 0, ans, [])
        return ans

    def backtrack(self, nums, i, ans, curr):
        if i >= len(nums):
            ans.append(list(curr))
            return

        curr.append(nums[i])
        self.backtrack(nums, i + 1, ans, curr)
        curr.pop()

        self.backtrack(nums, i + 1, ans, curr)
