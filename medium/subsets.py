from typing import List

""""""""""""""""""""""""""""
----------------------------------
OPTIMAL: OR approach
----------------------------------
TC: O(n*2ˆn)
SC: O(1)

-----------------
BETTER: Backtrack
-----------------
TC: O(n*2ˆn) - its n*2ˆn because `n` time is needed each time to copy the subset and we have 2 options.
SC: O(n); auxiliary stack space.

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.solve1(nums)
        return self.solve2(nums)

    # Approach 3: Using OR
    def or_approach(self, nums):
        n = len(nums)
        m = 2 ** n
        subs = []
        for i in range(0, m):
            sub = []
            for j in range(0, n):
                if self.bitset(i, j):
                    sub.append(nums[j])

            subs.append(sub)

        return subs

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
