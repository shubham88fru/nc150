from typing import List

# @link - https://neetcode.io/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.solve(nums)

    # Kadane's algorithm
    def solve(self, nums):
        n = len(nums)

        sm = 0
        max_sum = -9999999999
        for i in range(0, n):
            sm += nums[i]

            max_sum = max(max_sum, sm)

            # If subarray sum becomes -ve
            # then reset the sum coz, it will
            # only result in a reduced total sum
            # from this point on. We'd be better off
            # just summing the elements hereafter.
            if sm < 0:
                sm = 0

        return max_sum