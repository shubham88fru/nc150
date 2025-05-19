from typing import List

""""""""""""""""""""""""""""
-----------------------
OPTIMAL: Binary search.
-----------------------
TC: O(log(n))
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

---------------------
BRUTE: Linear search.
---------------------
TC: O(n)
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/find-target-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, target)

    def bs(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1