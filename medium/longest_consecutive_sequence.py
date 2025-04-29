from typing import List

""""""""""""""""""""""""""""
----------------
OPTIMAL: Hashset
----------------
TC: O(2n + n)
SC: O(n)

---------------
BETTER: Sorting
---------------
TC: O(nlog(n) + n)
SC: O(1)

--------------------------------------------------------------
BRUTE: Pick each number if keep checking if next can be found.
--------------------------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""

"""
Note that  in this problem, we are not supposed
find the longest consecutive subsequence, instead
the longest consecutive sequence that can be formed.
The subtle difference is that in the the next larger
number is not necessarily needed to be after the previous one.
The order in which elements appear in the array
doesn't matter for this problem.
"""
# @link - https://neetcode.io/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.solve(nums)
        # return self.approach2(nums)

    def solve(self, nums):
        st = set()
        for num in nums:
            st.add(num)

        longest = 0
        for num in nums:
            if num - 1 in st:
                continue

            nxt = num

            lngst = 0
            while nxt in st:
                nxt += 1
                lngst += 1
            longest = max(longest, lngst)

        return longest

    def approach2(self, nums):
        n = len(nums)
        if n == 0: return 0

        nums.sort()

        longest = 1
        curr = 1
        i = 1

        while i < n:
            if nums[i] == nums[i - 1]:
                i += 1
                continue

            if nums[i] == nums[i - 1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1

            i += 1

        return max(longest, curr)
