from typing import List

# @link - https://neetcode.io/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return self.solve(intervals)

    def solve(self, intervals):
        n = len(intervals);
        if n == 1:
            return 0

        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        rem = 0
        for i in range(1, n):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start < prev_end:
                rem += 1
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end

        return rem
