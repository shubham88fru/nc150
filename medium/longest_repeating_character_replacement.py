""""""""""""""""""""""""""""
-----------------------
OPTIMAL: Sliding window
-----------------------
TC: O(n)
SC: O(26)

-------------------------------------------------
BETTER: Sliding window with continuous freq check
-------------------------------------------------
TC: O(n*26)
SC: O(26)

---------------------------------------------------------------
BRUTE: Generate all substrings and and check maxFreq - len <= k
---------------------------------------------------------------
TC: O(n^2)
SC: O(26)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/longest-repeating-substring-with-replacement
# @check - https://www.youtube.com/watch?v=gqXU1UyA8pk&ab_channel=NeetCode
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0

        freq = {}
        maxLen = 0
        while r < n:
            ch = s[r]
            freq[ch] = freq.get(ch, 0) + 1

            windowSz = r - l + 1
            if windowSz - self.maxFreq(freq) > k:
                freq[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen

    def maxFreq(self, freq):
        return max(freq.values())
