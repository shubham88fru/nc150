import heapq
from typing import List

# @link - https://neetcode.io/problems/minimum-interval-including-query
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        return self.solve(intervals, queries)

    def solve(self, intervals, queries):
        n = len(queries)
        sorted_queries = []
        for i in range(n):
            sorted_queries.append([queries[i], i])
        sorted_queries.sort(key=lambda x: x[0])

        intervals.sort(key=lambda x: x[0])

        min_heap = []
        heapq.heapify(min_heap)

        ans = [-1] * n
        j = 0
        for i in range(n):

            while j < len(intervals):
                if intervals[j][0] <= sorted_queries[i][0] and intervals[j][1] >= sorted_queries[i][0]:
                    heapq.heappush(min_heap, [intervals[j][1] - intervals[j][0] + 1, intervals[j][1]])
                elif intervals[j][0] > sorted_queries[i][0]:
                    break

                j += 1

            while len(min_heap) > 0 and min_heap[0][1] < sorted_queries[i][0]:
                heapq.heappop(min_heap)

            if len(min_heap) > 0:
                ans[sorted_queries[i][1]] = min_heap[0][0]

        return ans