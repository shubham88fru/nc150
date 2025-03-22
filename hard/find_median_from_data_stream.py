import heapq

# @link - https://neetcode.io/problems/find-median-in-a-data-stream
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        if (len(self.max_heap) == 0 and len(self.min_heap) == 0):
            heapq.heappush(self.max_heap, (-num, num))
        else:
            if num <= self.max_heap[0][1]:
                heapq.heappush(self.max_heap, (-num, num))
            else:
                heapq.heappush(self.min_heap, num)

            if len(self.max_heap) > len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, heapq.heappop(self.max_heap)[1])
            elif len(self.min_heap) > len(self.max_heap):
                n = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-n, n))

    def findMedian(self) -> float:
        sz = len(self.min_heap) + len(self.max_heap)
        if sz % 2 == 0:
            return (self.min_heap[0] + self.max_heap[0][1]) / 2
        return self.max_heap[0][1]