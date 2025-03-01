import heapq
from typing import List

# @link - https://neetcode.io/problems/hand-of-straights
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        return self.solve(hand, groupSize)

    def solve(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True