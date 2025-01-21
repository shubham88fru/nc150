from typing import List

# @link - https://neetcode.io/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
