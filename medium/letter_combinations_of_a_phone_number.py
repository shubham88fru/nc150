from typing import List

""""""""""""""""""""""""""""
---------------------
OPTIMAL: Backtracking
---------------------
TC: O(n*4ˆn)
SC: O(n)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.revise(digits)

    def revise(self, digits):
        mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ans = []
        self.backtrack(digits, 0, ans, '', mp)
        return ans

    def backtrack(self, digits, i, ans, sub, mp):
        if i >= len(digits):
            ans.append(sub)
            return

        for el in mp[digits[i]]:
            self.backtrack(digits, i + 1, ans, sub + el, mp)
