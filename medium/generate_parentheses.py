from typing import List

""""""""""""""""""""""""""""
-------------------------------------
OPTIMAL: smart recursion/backtracking.
-------------------------------------
TC: O(2^2n)
SC: O(2n)

------------------------------------
BETTER: 
------------------------------------
TC:
SC:

----------------------------------------------------------------------------------
BRUTE: Generate all possible combinations and for each use stack to check if valid.
----------------------------------------------------------------------------------
TC: O(2n * 2^2n)
SC: O(2n) ; depth of recursive tree.

"""""""""""""""""""""""""""
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
