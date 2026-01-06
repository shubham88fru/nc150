from typing import List

""""""""""""""""""""""""""""
--------------------------
OPTIMAL: DP + Backtracking
--------------------------
TC: TC: O(nˆ2 + 2ˆn)
SC: O(n); recursive stack space

------------------------------------
BETTER: DFS/backtracking
------------------------------------
TC: TC: O(n*2ˆn)
SC: O(n); recursive stack space

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/palindrome-partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # return self.revise(s)
        return self.approach2(s)

    def approach2(self, s):
        n = len(s)

        palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    palindrome[i][j] = True

        for L in range(2, n + 1):
            for i in range(0, n - L + 1):
                j = i + L - 1
                if s[i] == s[j]:
                    if L == 2:
                        palindrome[i][j] = True
                    else:
                        palindrome[i][j] = palindrome[i + 1][j - 1]

        ans = []
        self.backtrack2(s, ans, [], palindrome, n, 0)
        return ans

    def backtrack2(self, s, ans, sub, palindrome, n, i):
        if i >= n:
            ans.append(sub[:])
            return

        for j in range(i, n):
            if palindrome[i][j]:
                sub.append(s[i: j + 1])
                self.backtrack2(s, ans, sub, palindrome, n, j + 1)
                sub.pop()

    def revise(self, s):
        n = len(s)

        ans = []
        self.backtrack(s, ans, [], n, 0)
        return ans

    def backtrack(self, s, ans, sub, n, i):
        if i >= n:
            ans.append(sub[:])
            return

        for j in range(i, n):
            if self.isPalindrome(s[i: j + 1]):
                sub.append(s[i: j + 1])
                self.backtrack(s, ans, sub, n, j + 1)
                sub.pop()

    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True