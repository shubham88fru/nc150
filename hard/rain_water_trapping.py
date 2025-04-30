from typing import List

""""""""""""""""""""""""""""
-------------------------------
OPTIMAL: Two pointers (striver)
-------------------------------
TC: O(n)
SC: O(1)

-----------------------------
BETTER: Prefix and suffix max
-----------------------------
TC: O(n + n + n)
SC: O(n + n)

-----------------------------------------------------------
BRUTE: For each building, find max to left and max to right
-----------------------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""


# @link - https://neetcode.io/problems/trapping-rain-water
def trap(self, height: List[int]) -> int:
    # return self.solve(height)
    return self.solve2(height)


# solve1 and solve2 are similar
# but solve2 is more intuitive to me.
def solve2(self, height):
    n = len(height)
    pm = [0] * n  # largest before curr
    sm = [0] * n  # largest after curr

    pm[0] = 0
    sm[n - 1] = 0
    for i in range(1, n):
        pm[i] = max(pm[i - 1], height[i - 1])

    for j in range(n - 2, -1, -1):
        sm[j] = max(height[j + 1], sm[j + 1])

    ans = 0
    for k in range(1, n - 1):
        if height[k] < pm[k] and height[k] < sm[k]:  # if curr is in between
            ans += (min(pm[k], sm[k]) - height[k])

    return ans


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
