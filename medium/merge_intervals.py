from typing import List

# @link - https://neetcode.io/problems/merge-intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.solve(intervals)

    def solve(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for i in range(0, len(intervals)):
            if len(merged) > 0 and intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged