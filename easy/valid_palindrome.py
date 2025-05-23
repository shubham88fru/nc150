""""""""""""""""""""""""""""
--------------------
OPTIMAL: Two pointer
--------------------
TC: O(n)
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

-----------------------------------------------------------------------------------------
BRUTE: For a new string by removing non alphanumeric characters, then reverse and compare
-----------------------------------------------------------------------------------------
TC: O(n+n)
SC: O(n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/is-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
