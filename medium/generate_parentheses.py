from typing import List

# @link - https://neetcode.io/problems/generate-parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.using_backtracking(n)

    def using_backtracking(self, n):
        ans = []
        self.backtrack(n, ans, "", 0, 0)
        return ans

    def backtrack(self, n, ans, curr, oc, cc):
        if oc == cc and oc == n:
            ans.append(curr)
            return

        if oc < n:
            self.backtrack(n, ans, curr + "(", oc + 1, cc)

        if cc < oc:
            self.backtrack(n, ans, curr + ")", oc, cc + 1)
