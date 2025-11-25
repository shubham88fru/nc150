import heapq
from typing import List

""""""""""""""""""""""""""""
-----------------
OPTIMAL: Max heap
-----------------
TC: O(n*log(n) + n * (3log(n)) --> O(4nlog(n))
SC: O(n)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

--------------------------------------------
BRUTE: Keep sorting and checking largest two
--------------------------------------------
TC: O(n*nlog(n))
SC: O(n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/last-stone-weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return self.revise(stones)

    def revise(self, stones):
        n = len(stones)
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            l = -heapq.heappop(heap)
            sl = -heapq.heappop(heap)

            if l == sl:
                continue

            heapq.heappush(heap, -abs(l - sl))

        return 0 if len(heap) == 0 else -heap[0]