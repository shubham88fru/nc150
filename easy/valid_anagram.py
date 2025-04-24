
# @link - https://neetcode.io/problems/is-anagram
""""""""""""""""""""""""""""

-----------------------------------------------------------------------------------------------------
FOLLOW UP: What if unicode char? --> 128 size array or a hashmap, increment for one and dec for other
-----------------------------------------------------------------------------------------------------
TC: O(n + n + n) if array, or O(n + n) if hashmap
SC: O(1)

--------------------------------------------
OPTIMAL: One 26 length freq array, +1 and -1
--------------------------------------------
TC: O(n + n + n) if array, or O(n + n) if hashmap
SC: O(1)

------------------------------------
BETTER: Two 26 length array of freqs.
------------------------------------
TC: O(n + n + n)
SC: O(1)

-----------------------------------------
BRUTE: Sort and compare letter by letter.
-----------------------------------------
TC: O(nlog(n) + n)
SC: O(1)

"""""""""""""""""""""""""""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = {}
        dic2 = {}
        for ch in s:
            dic1[ch] = dic1.get(ch, 0) + 1

        for ch in t:
            dic2[ch] = dic2.get(ch, 0) + 1

        for key in dic1.keys():
            if key not in dic2:
                return False
            if dic1.get(key) != dic2.get(key):
                return False

        return True
