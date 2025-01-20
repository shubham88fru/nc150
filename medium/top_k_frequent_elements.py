import heapq
from typing import List

# /**
#  * NOTE: Apparently there's a bucket sort solution as well
#  * or some solution with simple hashmap, which has a better TC
#  * than the heap solution. If this problem is a
#  * recurring problem for some company, check that approach
#  * as well.
#  */
# @link - https://neetcode.io/problems/top-k-elements-in-list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += + 1

        tpl = [(count, el) for el, count in freq.items()]

        heap = []
        for item in tpl:
            if len(heap) < k:
                heapq.heappush(heap, item)
            elif item[0] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, item)

        return [t[1] for t in heap]