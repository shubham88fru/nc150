# @link - https://neetcode.io/problems/valid-parenthesis-string
class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.solve(s)

    # Approach 1: There's a liner time
    # greedy soln for this problem.
    # But its nasty and there's no way
    # I'll be able to do it in an interview.
    # So leaving it for now.

    # Approach 2: My dp and memo soln.
    def solve(self, s):
        return self.dp(s, 0, 0, {})

    def dp(self, s, i, oc, cache):
        if i >= len(s) and oc == 0:
            return True

        if i >= len(s):
            return False

        if (oc < 0):
            return False

        k = str(i) + "_" + str(oc)
        if k in cache:
            return cache[k]

        ch = s[i]

        normal = False
        wild = False
        if ch == '*':
            wild = self.dp(s, i + 1, oc, cache) or self.dp(s, i + 1, oc - 1, cache) or self.dp(s, i + 1, oc + 1, cache)
        elif ch == '(':
            normal = self.dp(s, i + 1, oc + 1, cache)
        else:
            normal = self.dp(s, i + 1, oc - 1, cache)

        cache[k] = normal or wild
        return cache[k]
