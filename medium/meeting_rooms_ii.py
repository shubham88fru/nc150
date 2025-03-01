
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        return self.solve(intervals)

    # The problem is basically asking to
    # find the maximum number of overlapping
    # intervals. Because the maximum overlapping
    # meeting intervals will be the minimum num
    # of meeting rooms required.
    def solve(self, intervals):
        n = len(intervals)
        start = []
        end = []
        for ivl in intervals:
            start.append(ivl.start)
            end.append(ivl.end)

        start.sort()
        end.sort()

        max_rooms =0
        rooms = 0
        p1 = 0
        p2 = 0
        while p1 < n and p2 < n:
            if start[p1] < end[p2]: #a meeting started
                rooms += 1
                p1 += 1
                max_rooms = max(max_rooms, rooms)
            else:
                rooms -= 1
                p2 += 1

        return max_rooms