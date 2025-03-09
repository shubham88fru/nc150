from typing import List


# @link - https://neetcode.io/problems/count-squares
class CountSquares:

    def __init__(self):
        self.mp = {}
        self.lst = []

    def add(self, point: List[int]) -> None:
        self.mp[tuple(point)] = self.mp.get(tuple(point), 0) + 1
        self.lst.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        ans = 0

        for x, y in self.lst:
            # key observation. without which the problem is
            # very difficult. Find the diagonal and then finding
            # the other two points will be much easier.
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue

            ans += (self.mp.get((x, py), 0) * self.mp.get((px, y), 0))

        return ans