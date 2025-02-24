from typing import List

# @link - https://neetcode.io/problems/combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.solve(digits)

    def solve(self, digits):
        mp = {}
        mp['2'] = ['a', 'b', 'c']
        mp['3'] = ['d', 'e', 'f']
        mp['4'] = ['g', 'h', 'i']
        mp['5'] = ['j', 'k', 'l']
        mp['6'] = ['m', 'n', 'o']
        mp['7'] = ['p', 'q', 'r', 's']
        mp['8'] = ['t', 'u', 'v']
        mp['9'] = ['w', 'x', 'y', 'z']

        ans = []
        if len(digits) == 0:
            return ans

        self.backtrack(digits, 0, ans, "", mp)

        return ans

    def backtrack(self, digits, wi, ans, curr, mp):
        if wi >= len(digits):
            ans.append(curr)
            return

        lst = mp[digits[wi]]

        for i in range(0, len(lst)):
            self.backtrack(digits, wi+1, ans, curr+lst[i], mp)