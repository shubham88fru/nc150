import heapq
from typing import List

""""""""""""""""""""""""""""
-------------------------------------------
OPTIMAL: map and bucket array (bucket sort)
-------------------------------------------
TC: O(n)
SC: O(d + n)

------------------------
BETTER: min heap and map
------------------------
TC: O(n*klog(k)) ;
SC: O(k)

------------------------------------------------------
BRUTE: Hashmap for freq --> to list of tuples --> sort.
------------------------------------------------------
TC: O(n + d + dlog(d)) ; d is the number of distinct elements
SC: O(2*d)

"""""""""""""""""""""""""""

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