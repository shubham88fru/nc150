import heapq

""""""""""""""""""""""""""""
------------------
OPTIMAL: Two heaps
------------------
TC: O(log(n))
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

------------------------------------
BRUTE: Sort everytime a num is added
------------------------------------
TC: O(nlog(n))
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/find-median-in-a-data-stream
class MedianFinder:

    def __init__(self):
        self.mih = []
        self.mxh = []

    # Coded based on mik's approach.
    def addNum(self, num: int) -> None:
        if len(self.mxh) == 0 or num <= -self.mxh[0]:
            heapq.heappush(self.mxh, -num)
        else:
            heapq.heappush(self.mih, num)

        if len(self.mih) > len(self.mxh):
            heapq.heappush(self.mxh, -heapq.heappop(self.mih))
        elif len(self.mxh) - len(self.mih) > 1:
            heapq.heappush(self.mih, -heapq.heappop(self.mxh))

    def findMedian(self) -> float:
        if (len(self.mih) + len(self.mxh)) % 2 == 0:
            return (self.mih[0] - self.mxh[0]) / 2

        return -self.mxh[0]