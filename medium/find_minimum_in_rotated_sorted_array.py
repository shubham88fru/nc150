from typing import List

# @link - https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.bs(nums)

    def bs(self, nums):
        n = len(nums)

        l = 0
        r = n - 1

        mini = nums[0]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]:
                mini = min(mini, nums[l])
                l = mid + 1
            else:
                mini = min(nums[mid], mini)
                r = mid - 1

        return mini