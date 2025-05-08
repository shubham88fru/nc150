
# @link - https://neetcode.io/problems/longest-substring-without-duplicates
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.pass1(s)
        # return self.pass2(s)
        # return self.revise(s)
        return self.revise2(s)

    # Soln based on the new sliding
    # window template.
    def revise2(self, s):
        mp = {}
        n = len(s)

        l = 0
        r = 0
        mx = 0
        while r < n:
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1

            mp[s[r]] = r
            mx = max(mx, r - l + 1)
            r += 1

        return mx

    def revise(self, s):
        mp = {}
        n = len(s)

        l = 0
        r = 0
        mx = 0
        while r < n:
            if s[r] not in mp:
                mp[s[r]] = 0

            mp[s[r]] += 1
            while mp[s[r]] > 1:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1

            mx = max(mx, r - l + 1)
            r += 1

        return mx

    # A bit ineffecient when
    # removing repeated char.
    def pass1(self, s):
        n = len(s)
        l = 0
        r = 0

        window = {}
        maxLen = 0;
        while r < n:
            ch = s[r]
            if ch not in window:
                window[ch] = window.get(ch, 0) + 1  # store the freq.
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                while l <= r and ch in window:
                    chl = s[l]
                    window[chl] -= 1
                    if window[chl] == 0:
                        del window[chl]
                    l += 1
        return maxLen

    def pass2(self, s):
        n = len(s)
        l = 0
        r = 0

        window = {}
        maxLen = 0;
        while r < n:
            ch = s[r]
            if ch not in window or window[ch] < l:  # even if in map, but not in current window, we are good.
                window[ch] = r  # store the index of occurrence.
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                l = window[ch] + 1  # move l after the index of last occurence.
        return maxLen
