import heapq
from typing import List

""""""""""""""""""""""""""""
--------------------------
OPTIMAL: Quick select algo
--------------------------
TC: O(n) on average but worst case can be O(nˆ2)
SC: O(1); in-place algo.

----------------
BETTER: Min heap
----------------
TC: O(nlog(k))
SC: O(k)

--------------
BRUTE: Sorting
--------------
TC: O(nlog(n))
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heap_sol(nums, k)

    # Following is a heap soln,
    # but there's a popular quick
    # select algo which mik showed.
    # Was too lazy to code it but
    # its definitely an approach
    # worth knowing because of its
    # TC benefits.
    def heap_sol(self, nums, k):
        n = len(nums)

        heap = []
        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]