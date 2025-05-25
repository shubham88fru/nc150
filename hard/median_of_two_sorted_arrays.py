from typing import List

""""""""""""""""""""""""""""
----------------------
OPTIMAL: Binary search
----------------------
TC: O(log(min(m, n))
SC: O(1)

-------------------------------------------------------------------------
BETTER: Merge two sorted arrays keeping track of middle and second middle
-------------------------------------------------------------------------
TC: O(m + n)
SC: O(1)

---------------------------------------------
BRUTE: Merge two sorted arrays in third array
---------------------------------------------
TC: O(m + n)
SC: O(m + n)

-------------------------------------------------
DUMB: Copy both to new array as is, and then sort
-------------------------------------------------
TC: O(m+n) + O((m+n)log(m+n))
SC: O(m+n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.solve(nums1, nums2)

    # 1) Optimal solution.
    # Based on mik's explanation
    # Check java soln for comments and link for revision.
    def optimal(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 >= n2:
            return self.binary_search(nums2, nums1)

        return self.binary_search(nums1, nums2)

    def binary_search(self, a, b):
        n1 = len(a)
        n2 = len(b)
        total_left = (n1 + n2 + 1) // 2

        l = 0
        r = n1

        while l <= r:
            a_left_count = l + (r - l) // 2
            b_left_count = total_left - a_left_count

            al = -9999999999
            bl = -9999999999
            ar = 9999999999
            br = 9999999999

            if a_left_count > 0:
                al = a[a_left_count - 1]
            if a_left_count < n1:
                ar = a[a_left_count]
            if b_left_count > 0:
                bl = b[b_left_count - 1]
            if b_left_count < n2:
                br = b[b_left_count]

            if al <= br and bl <= ar:
                if (n1 + n2) % 2 != 0:
                    return max(al, bl)
                return (max(al, bl) + min(ar, br)) / 2

            if al > br:
                r = a_left_count - 1
            else:
                l = a_left_count + 1

        return 0.0

    # 2) This is a better soln - not optimal.
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