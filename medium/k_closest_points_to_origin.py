import heapq
from typing import List


# @link - https://neetcode.io/problems/k-closest-points-to-origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for i in range(0, len(points)):

            point = points[i]
            curr_dist = (point[0] * point[0] + point[1] * point[1])
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-curr_dist, (point[0], point[1])))
            elif curr_dist < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-curr_dist, (point[0], point[1])))

        return [[x, y] for _, (x, y) in max_heap]