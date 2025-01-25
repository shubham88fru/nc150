
# @link - https://neetcode.io/problems/longest-repeating-substring-with-replacement
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
