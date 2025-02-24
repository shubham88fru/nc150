from typing import List

# @link - https://neetcode.io/problems/palindrome-partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.solve(s)

    def solve(self, s):
        ans = []
        self.backtrack(s, ans, [])
        return ans

    def backtrack(self, s, ans, curr):
        if len(s) == 0:
            ans.append(list(curr))
            return

        for i in range(0, len(s)):
            sub = s[0: i + 1]
            if self.palindrome(sub):
                curr.append(sub)
                self.backtrack(s[i + 1: len(s)], ans, curr)
                curr.pop()

    def palindrome(self, sub):
        l = 0
        r = len(sub) - 1

        while l <= r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1

        return True