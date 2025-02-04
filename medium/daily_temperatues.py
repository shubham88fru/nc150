from typing import List

#@link - https://neetcode.io/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return self.optimal(temperatures)
        return self.simplified_optimal(temperatures)

    def simplified_optimal(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(0, n):
            curr = temperatures[i]
            while len(stack) > 0 and curr > stack[-1][0]:
                rem = stack.pop()
                ans[rem[1]] = i - rem[1]
            stack.append([curr, i])

        return ans

    def optimal(self, temperatures):
        n = len(temperatures)
        ans = [0] * n

        stack = []
        for i in range(0, n):
            curr = temperatures[i]
            if len(stack) == 0:
                stack.append([curr, i])
            elif curr <= stack[-1][0]:
                stack.append([curr, i])
            else:
                while len(stack) > 0 and curr > stack[-1][0]:
                    rem = stack.pop()
                    ans[rem[1]] = i - rem[1]
                stack.append([curr, i])

        return ans