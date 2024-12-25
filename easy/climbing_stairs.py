# @link - https://neetcode.io/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs(n)

    def dfs(self, n):
        if n < 0:
            return 0

        if n == 0:
            return 1

        one = 0
        one += self.dfs(n - 1)

        two = 0
        two += self.dfs(n - 2)

        return one + two