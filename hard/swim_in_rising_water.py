import heapq
from typing import List

# @link - https://neetcode.io/problems/swim-in-rising-water
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        return self.solve(grid)

    def solve(self, grid):
        n = len(grid)
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[0][0] = -1

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = 999999999

        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, [grid[0][0], 0, 0])

        while min_heap:
            mx, i, j = heapq.heappop(min_heap)
            if i == n-1 and j == n-1:
                ans = min(ans, mx)
                continue

            visited[i][j] = -1

            for di in dirs:
                ni = i + di[0]
                nj = j + di[1]

                if ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj] == -1:
                    continue

                heapq.heappush(min_heap, [max(mx, grid[ni][nj]), ni, nj])

        return ans