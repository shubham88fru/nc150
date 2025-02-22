import heapq
from typing import List

# @link - https://neetcode.io/problems/task-scheduling
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return self.solve(tasks, n)

    # Following is my approach using min heap.
    # NC showed a solution using max heap which
    # has a better TC. Also showed brute and greedy.
    # Check those soln if this is a recurring problem
    # for some company.
    def solve(self, tasks, n):
        minTime = [0] * 26
        min_heap = []
        for i in range(0, len(tasks)):
            ch = tasks[i]
            if minTime[ord(ch) - ord('A')] == 0:
                minTime[ord(ch) - ord('A')] += 1
            else:
                minTime[ord(ch) - ord('A')] += 1 + n

            heapq.heappush(min_heap, minTime[ord(ch) - ord('A')])

        time = 0
        while len(min_heap) > 0:
            if time < min_heap[0]:
                time += (min_heap[0] - time)
            else:
                time += 1

            heapq.heappop(min_heap)

        return time