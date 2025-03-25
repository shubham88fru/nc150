from typing import List

# @link - https://neetcode.io/problems/trapping-rain-water
def trap(self, height: List[int]) -> int:
    return self.solve(height)

def solve(self, height):
    n = len(height)
    pm = [0] * n
    sm = [0] * n

    pm[0] = height[0]
    sm[n - 1] = height[n - 1]
    for i in range(1, n):
        pm[i] = max(pm[i - 1], height[i])

    for j in range(n - 2, -1, -1):
        sm[j] = max(height[j], sm[j + 1])

    ans = 0
    for k in range(0, n):
        ans += (min(pm[k], sm[k]) - height[k])

    return ans