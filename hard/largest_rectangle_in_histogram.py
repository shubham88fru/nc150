from typing import List

# @link - https://neetcode.io/problems/largest-rectangle-in-histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.solve(heights)

    # 2) This ain't the bestest and most
    # optimal approach either. However, to me its the most
    # intuitive soln. For the most optimal approach,
    # check my java soln.
    def solve(self, heights):
        n = len(heights)
        lb = [0] * n
        rb = [0] * n

        self.fillLb(heights, lb)
        self.fillRb(heights, rb)

        max_area = -9999999999
        for i in range(0, n):
            max_area = max(max_area, (rb[i] - lb[i] + 1) * heights[i])

        return max_area

    def fillLb(self, heights, lb):
        n = len(heights)
        stack = []

        for i in range(n):
            if len(stack) == 0:
                stack.append(0)
                lb[i] = 0
            else:
                while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                    stack.pop()

                if len(stack) == 0:
                    lb[i] = 0
                    stack.append(i)
                else:
                    lb[i] = stack[-1] + 1
                    stack.append(i)

    def fillRb(self, heights, rb):
        n = len(heights)
        stack = []

        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                stack.append(n - 1)
                rb[i] = n - 1
            else:
                while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                    stack.pop()

                if len(stack) == 0:
                    rb[i] = n - 1
                    stack.append(i)
                else:
                    rb[i] = stack[-1] - 1
                    stack.append(i)

    # 3) Brute force is to iterate through the heights
    # and for each height, find the left boundary i.e.
    # the closest element on the left that is smaller
    # and the right boundary i.e. the closest elment on
    # the right that is smaller than the current element.
    # Keep taking max.