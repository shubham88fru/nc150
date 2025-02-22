import heapq
from typing import List

# @link - https://neetcode.io/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k)

    def solve(self, nums, k):
        min_heap = []

        for i in range(0, len(nums)):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[i])
            elif nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])

        return min_heap[0]