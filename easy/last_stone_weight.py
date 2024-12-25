import heapq
from typing import List

# @link - https://neetcode.io/problems/last-stone-weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Trick for max heap in python
        # unlike java, max heap doesn't come
        # out of the box in python.
        mx_heap = [ -stone for stone in stones ]
        heapq.heapify(mx_heap)
        while len(mx_heap) != 0:
            if len(mx_heap) > 1:
                s = heapq.heappop(mx_heap)
                ss = heapq.heappop(mx_heap)
                if s != ss:
                    heapq.heappush(mx_heap, -abs(s-ss))
            else:
                return abs(heapq.heappop(mx_heap))

        return 0