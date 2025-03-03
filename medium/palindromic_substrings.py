# @link - https://neetcode.io/problems/palindromic-substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.solve(s)

    def solve(self, s):
        n = len(s)

        dp = {}
        count = 0
        for i in range(0, n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j, dp):
                    count += 1

        return count

    def isPalindrome(self, s, i, j, dp):
        if i >= j:
            return True

        k = str(i) + "_" + str(j)
        if k in dp:
            return dp[k]

        if s[i] == s[j]:
            ans = self.isPalindrome(s, i + 1, j - 1, dp)
            dp[k] = ans
            return ans

        dp[k] = False
        return False