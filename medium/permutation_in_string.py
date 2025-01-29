# @link - https://neetcode.io/problems/permutation-string
def checkInclusion(self, s1: str, s2: str) -> bool:
    if (len(s1) > len(s2)):
        return False

    ogFreq = {}
    for i in range(0, len(s1)):
        ogFreq[s1[i]] = ogFreq.get(s1[i], 0) + 1

    l = 0
    r = 0
    n = len(s2)

    window = dict(ogFreq)
    while r < n:
        ch = s2[r]
        if ch in window:
            r += 1
            window[ch] = window.get(ch) - 1
            if window[ch] == 0:
                del window[ch]
            if r - l == len(s1) and len(window) == 0:
                return True
        else:
            if l == r:
                l += 1
                r += 1
            else:
                rem = s2[l]
                l += 1
                if rem in ogFreq:
                    window[rem] = window.get(rem, 0) + 1

    return False