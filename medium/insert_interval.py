from typing import List

# @link - https://neetcode.io/problems/insert-new-interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.solve(intervals, newInterval)

    def solve(self, intervals, newInterval):
        after_insert = []
        inserted = False
        for i in range(0, len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                after_insert.append(newInterval)
                inserted = True
            after_insert.append(intervals[i])

        if not inserted:
            after_insert.append(newInterval)

        merged = []
        for i in range(0, len(after_insert)):
            if len(merged) > 0 and after_insert[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], after_insert[i][1])
            else:
                merged.append(after_insert[i])

        return merged
