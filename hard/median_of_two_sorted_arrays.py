from typing import List

# @link - https://neetcode.io/problems/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.solve(nums1, nums2)

    # 1) Optimal solution.

    # 2) This is a better soln - not optimal.
    # Optimal solutions is O(log(m+n)) and uses
    # binary search. But its a bit confusing so
    # will need to rewatch strvr to figure it out
    # again.
    def solve(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        n = n1 + n2

        midi = -1
        smidi = -1
        mid = -1
        smid = -1

        if n % 2 != 0:
            midi = n // 2
        else:
            midi = n // 2 - 1
            smidi = n // 2

        i1 = 0
        i2 = 0
        k = 0
        while i1 < n1 and i2 < n2:
            if num1[i1] < num2[i2]:
                if k == midi:
                    mid = num1[i1]
                elif k == smidi:
                    smid = num1[i1]
                i1 += 1
            else:
                if k == midi:
                    mid = num2[i2]
                elif k == smidi:
                    smid = num2[i2]
                i2 += 1

            k += 1

        while i1 < n1:
            if k == midi:
                mid = num1[i1]
            elif k == smidi:
                smid = num1[i1]
            i1 += 1
            k += 1

        while i2 < n2:
            if k == midi:
                mid = num2[i2]
            elif k == smidi:
                smid = num2[i2]
            i2 += 1
            k += 1

        return mid if n % 2 != 0 else (mid + smid) / 2