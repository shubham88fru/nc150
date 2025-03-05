from typing import List

# @link - https://neetcode.io/problems/maximum-product-subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.solve(nums)

    def solve(self, nums):
        n = len(nums)

        prefix = 1
        suffix = 1

        mx = -9999999999
        for i in range(0, n):
            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

            mx = max(mx, max(prefix, suffix))

        return mx