# @link - https://neetcode.io/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve(s)

    # Note how memoization is
    # done in the palindrome check func
    # and is not part of the actual problem.
    # This is a unique dp problem (for me) since
    # it doesn't follow the 01 knapsack pattern as
    # most dp problems do.
    def solve(self, s):
        n = len(s)
        dp = {}

        MAX = -999999
        start = 0
        end = 0
        for i in range(0, n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j, dp):
                    if j-i+1 > MAX:
                        MAX = j-i + 1
                        start = i
                        end = j

        return s[start:end+1]

    def isPalindrome(self, s, i, j, dp):
        if i >= j:
            return True

        k = str(i) + "_" + str(j)
        if k in dp:
            return dp[k]

        if (s[i] == s[j]):
            ans = self.isPalindrome(s, i+1, j-1, dp)
            dp[k] = ans
            return ans

        dp[k] = False
        return False