from typing import List

# @link - https://neetcode.io/problems/products-of-array-discluding-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
