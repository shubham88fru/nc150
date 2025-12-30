from typing import List

""""""""""""""""""""""""""""
------------------------------
OPTIMAL: Recursion without set
------------------------------
TC: O(n!*n)
SC: O(n); recursive stack space.

--------------------------
BETTER: Recursion with set
--------------------------
TC: O(n!*n)
SC: O(2n); stack + set

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.solve(nums)

    def solve(self, nums):
        ans = []
        # self.backtrack(nums, ans, [], set())
        # self.swap_recursion1(0, ans, nums[:])
        self.swap_recursion2(0, ans, nums)
        return ans

    def swap_recursion2(self, idx, ans, nums):
        if idx >= len(nums):
            ans.append(nums[:])
            return

        for i in range(idx, len(nums)):
            self.swap2(nums, idx, i)  # swap `idx` with `i` and explore.
            self.swap_recursion2(idx + 1, ans, nums)
            self.swap2(nums, i, idx)

    def swap_recursion1(self, idx, ans, perm):
        if idx >= len(perm):
            ans.append(perm[:])
            return

        for i in range(idx, len(perm)):
            self.swap_recursion1(idx + 1, ans, self.swap1(perm, idx, i))

    def backtrack(self, nums, ans, perm, st):
        if len(perm) == len(nums):
            ans.append(perm[:])
            return

        for i in range(0, len(nums)):
            if i in st:
                continue

            st.add(i)
            perm.append(nums[i])
            self.backtrack(nums, ans, perm, st)
            st.remove(i)
            perm.pop()

    def swap1(self, perm, i, j):
        cpy = perm[:]
        t = cpy[i]
        cpy[i] = cpy[j]
        cpy[j] = t
        return cpy

    # in-place swap nums
    def swap2(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t