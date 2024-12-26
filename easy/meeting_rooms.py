"""
Definition of Interval:
"""
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# @link - https://neetcode.io/problems/meeting-schedule
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        srtd = sorted(intervals, key=lambda x: x.start)
        for idx, _ in enumerate(srtd):
            if idx == 0:
                continue

            if srtd[idx].start < srtd[idx - 1].end:
                return False

        return True
