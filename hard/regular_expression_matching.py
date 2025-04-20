# @link - https://neetcode.io/problems/regular-expression-matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s, p)

    def solve(self, s, p):
        return self.recursion(s, p)

    def recursion(self, s, p):
        if len(p) == 0:
            return len(s) == 0

        fmatch = len(s) != 0 and (s[0] == p[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            take_astrx = fmatch and self.recursion(s[1:], p)
            not_take_astrx = self.recursion(s, p[2:])

            return take_astrx or not_take_astrx
        else:
            return fmatch and self.recursion(s[1:], p[1:])