import heapq
from typing import List

""""""""""""""""""""""""""""
---------------
OPTIMAL: Greedy
---------------
TC: O(n)
SC: O(1)

----------------
BETTER: Max heap
----------------
TC: O(n)
SC: O(1)

---------------
BRUTE: Min heap
---------------
TC: O(nlog(n))
SC: O(n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/task-scheduling
# @check (greedy) - https://www.youtube.com/watch?v=QDsFBLGL9MM
# @check (max heap) - https://www.youtube.com/watch?v=rYh-Kkbzsnw
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # return self.min_heap(n, tasks)
        # return self.max_heap(n, tasks)
        return self.greedy(n, tasks)

    def greedy(self, n, tasks):
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        freq.sort()

        max_freq = max(freq)
        empty_groups = max_freq - 1
        empty_slots = n * empty_groups

        for i in range(24, -1, -1):
            empty_slots -= min(freq[i], empty_groups)

        if empty_slots > 0:
            return len(tasks) + empty_slots

        return len(tasks)

    def max_heap(self, n, tasks):
        freq = [0] * 26
        heap = []

        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        for i in range(26):
            if (freq[i] > 0):
                heapq.heappush(heap, -freq[i])

        cycles = 0
        while heap:
            batch = n + 1
            updatedFreqs = []
            while batch and heap:
                batch -= 1
                f = -heapq.heappop(heap)
                updatedFreqs.append(f - 1)

            for ff in updatedFreqs:
                if ff > 0:
                    heapq.heappush(heap, -ff)

            cycles += (n + 1) if heap else len(updatedFreqs)

        return cycles

    # Following is my approach using min heap.
    # NC showed a solution using max heap which
    # has a better TC. Also showed brute and greedy.
    # Check those soln if this is a recurring problem
    # for some company.
    # Edctv also a has a different soln that runs faster
    # than my approach (check my java solns for edctv)
    def min_heap(self, n, tasks):
        priority = [0] * 26
        heap = []

        for t in tasks:
            i = ord(t) - ord('A')
            f = priority[i]
            heapq.heappush(heap, (f, t))
            priority[i] += (1 + n)

        cycles = 0
        while heap:
            p = heapq.heappop(heap)[0]
            if p > cycles:
                cycles += (p - cycles + 1)
            else:
                cycles += 1

        return cycles