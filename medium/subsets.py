from typing import List

# @link - https://neetcode.io/problems/subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.solve1(nums)
        return self.solve2(nums)

    # Approach 2: makes subsets II problem straightforward.
    def solve2(self, nums):
        ans = []
        self.bactrack2(nums, 0, ans, [])
        return ans

    def bactrack2(self, nums, idx, ans, curr):
        ans.append(list(curr))

        for i in range(idx, len(nums)):
            curr.append(nums[i])
            self.bactrack2(nums, i + 1, ans, curr)
            curr.pop()

    # Approach 1: This is the first approach (based on 01 Knapsack pattern)
    # that comes to my mind whenever I encounter this problem.
    # However, this approach would lead a complicated (and nasty)
    # code for subsets II problem. So, as a rule of thumb always
    # solve it using the approach 2.
    def solve1(self, nums):
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
