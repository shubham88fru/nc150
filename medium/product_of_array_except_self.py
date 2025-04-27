from typing import List

# @link - https://neetcode.io/problems/products-of-array-discluding-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.revise(nums)

    # One pass.
    def revise(self, nums):
        n = len(nums)
        pp = [0] * n
        sp = [0] * n

        pp[0] = 1
        sp[n - 1] = 1

        for i in range(1, n):
            pp[i] = pp[i - 1] * nums[i - 1];
            sp[n - i - 1] = sp[n - i] * nums[n - i]

        ans = []
        for i in range(0, n):
            ans.append(pp[i] * sp[i])

        return ans

    # Two pass.
    def solve(self, nums):
        pp = [1]
        for i, el in enumerate(nums):
            pp.append(el * pp[len(pp) - 1])

        sp = [1]
        # trick to iterate a list in reverse.
        for i in range(len(nums) - 1, -1, -1):
            sp.append(nums[i] * sp[len(sp) - 1])

        sp.reverse()

        ans = []
        for i, _ in enumerate(nums):
            ans.append(pp[i] * sp[i + 1])

        return ans
