from typing import List

# @link - https://neetcode.io/problems/permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.solve(nums)

    def solve(self, nums):
        ans = []
        self.backtrack(nums, ans, [], set())
        return ans

    def backtrack(self, nums, ans, curr, st):
        if len(curr) == len(nums):
            ans.append(list(curr))
            return

        for i in range(0, len(nums)):
            if i in st:
                continue

            st.add(i)
            curr.append(nums[i])
            self.backtrack(nums, ans, curr, st)
            st.remove(i)
            curr.pop()