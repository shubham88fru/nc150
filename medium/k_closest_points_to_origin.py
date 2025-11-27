import heapq
import math
from typing import List

""""""""""""""""""""""""""""
---------------------------------
OPTIMAL: Using quick select algo
--------------------------------
TC: ??
SC: ??

--------------
GOOD: Max heap
--------------
TC: O(nlog(k))
SC: O(k)

------------------------------
BETTER: Min heap using heapify
------------------------------
TC: O(klog(n)) ; note, the TC will be O(n) for heapify op, 
    as opposed to normal loop to put elements to heap (which will be a O(nlog(n))) op.
SC: O(n)

--------------
BRUTE: Sorting
--------------
TC: O(nlog(n))
SC: O(1)

"""""""""""""""""""""""""""

# @link - https://neetcode.io/problems/k-closest-points-to-origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.revise(points, k)

    # This is a max heap soln.
    # Turns out there's an even better soln
    # using some `quick select` algorithm
    def revise(self, points, k):
        n = len(points)

        heap = []
        for p in points:
            heapq.heappush(heap, (-(math.pow(p[0], 2) + math.pow(p[1], 2)), p))

            if (len(heap) > k):
                pp = heapq.heappop(heap)

        ans = []
        while len(heap) > 0:
            ans.append(heapq.heappop(heap)[1])

        return ans