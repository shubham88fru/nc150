import heapq
from typing import List

""""""""""""""""""""""""""""
-----------------
OPTIMAL: Min heap
-----------------
TC: O(nlog(k))
SC: O(k)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

---------------------------------------------
BRUTE: Sorting each time and return kth index
---------------------------------------------
TC: O(nlog(n))
SC: O(n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/kth-largest-integer-in-a-stream
class KthLargest:
    # Style 1
    # Clever heap code.
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > k:  # clever
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: # clever
            heapq.heappop(self.heap)

        return self.heap[0]

    # Style 2
    # Note needless heap ops.
    def __init__1(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            elif n > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
