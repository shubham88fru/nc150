# @link - https://neetcode.io/problems/minimum-window-with-characters
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.solve(s, t)

    def solve(self, s, t):
        m = len(s)
        n = len(t)

        if m < n:
            return ""

        window = {}
        req_freq = {}
        for i in range(n):
            req_freq[t[i]] = req_freq.get(t[i], 0) + 1
            window[t[i]] = 0

        sub = [-1, -1]
        min_len = 999999999
        window_cnt = 0

        l = 0
        r = 0
        while r < m:
            ch = s[r]
            if ch in window:
                window[ch] += 1
                if window[ch] == req_freq[ch]:
                    window_cnt += 1

            while window_cnt == len(req_freq):
                ln = r - l + 1
                if ln < min_len:
                    min_len = ln
                    sub[0] = l
                    sub[1] = r

                ch_rem = s[l]
                if ch_rem in window and window[ch_rem] > 0:
                    window[ch_rem] -= 1
                    if window[ch_rem] < req_freq[ch_rem]:
                        window_cnt -= 1
                l += 1
            r += 1

        return "" if min_len == 999999999 else s[sub[0]:sub[1] + 1]