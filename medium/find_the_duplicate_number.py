""""""""""""""""""""""""""""
-------------------------------------------
ADVANCED: Tortoise and hare (fast and slow)
-------------------------------------------
TC: O(N)
SC: O(1)

--------------------
OPTIMAL: Cyclic sort
--------------------
TC: O(N)
SC: O(1)

-----------------------
BETTER: Hashmap/Hashset
-----------------------
TC: O(N)
SC: (N)

----------------------------------------
BRUTE 2: Sort and search
----------------------------------------
TC: O(Nlog(N) + N)
SC: O(1)

----------------------------------------
BRUTE 1: For each, check if we have copy
----------------------------------------
TC: O(N^2)
SC: O(1)

"""""""""""""""""""""""""""
from typing import List

# @link - https://neetcode.io/problems/find-duplicate-integer
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.solve(nums)

    # Approch 1 - Using cyclic sort technique.
    # However, there's a technique to solve
    # this q using linked list (fast and slow) pointers.
    # Check my java soln for that and do it in python.
    def solve(self, nums):
        n = len(nums)
        i = 0
        while (i < n):
            if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                targetIdx = nums[i] - 1
                temp = nums[targetIdx]
                nums[targetIdx] = nums[i]
                nums[i] = temp
            else:
                i += 1

        return nums[n - 1]