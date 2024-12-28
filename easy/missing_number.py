from typing import List


# @link - https://neetcode.io/problems/missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ts = sum(nums)
        n = len(nums)
        tsf = n*(n+1)//2
        return tsf-ts