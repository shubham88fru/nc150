from typing import List

# @link - https://neetcode.io/problems/max-water-container
def maxArea(self, heights: List[int]) -> int:
    # return self.brute(heights)
    return self.optimal(heights)


def optimal(self, height):
    i = 0
    j = len(height) - 1

    mx = 0
    while i < j:
        mx = max(mx, min(height[i], height[j]) * (j - i))
        if height[i] > height[j]:
            # Vice-versa of the below
            # explanation.
            j -= 1
        else:
            # If the left end is smaller (or equal)
            # than the right end, then there's no
            # way the left end will form
            # a larger area with any pillar
            # earlier than the current right
            # end.
            i += 1

    return mx


def brute(self, heights):
    mx = 0

    for i in range(0, len(heights) - 1):
        for j in range(i + 1, len(heights)):
            mx = max(mx, min(heights[i], heights[j]) * (j - i))

    return mx