""""""""""""""""""""""""""""
----------------
OPTIMAL: Sliding window
----------------
TC: O(m + n) where m and n are the lengths of the the strings.
SC: O(26)

-------------------------------------------------------------------------
BETTER: generate s1 length subs of s2 and keep checking against sorted s1
-------------------------------------------------------------------------
TC: O(nlog(n)*(m-n) + nlog(n))
SC: O(1)

-------------------------------------------------------------------
BRUTE: Generate all perms of s1 and keep checking if present in s2.
-------------------------------------------------------------------
TC: O(n! * n) where n is the length of s1
SC: O(n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/permutation-string
def checkInclusion(self, s1: str, s2: str) -> bool:
    # return self.oldSlidingWindowTemplate(s1, s2)
    return self.slidingWindow(s1, s2)

# using the better sliding widow template.
def slidingWindow(self, s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    if n2 < n1:
        return False

    s1_mp = [0] * 26
    for ch in s1:
        s1_mp[ord(ch) - ord('a')] += 1

    l = 0
    r = 0
    window = [0] * 26
    while r < n2:
        ch = s2[r]
        window[ord(ch) - ord('a')] += 1
        while window[ord(ch) - ord('a')] > s1_mp[ord(ch) - ord('a')]:
            window[ord(s2[l]) - ord('a')] -= 1
            l += 1

        all_same = True
        for i in range(0, 26):
            if s1_mp[i] != window[i]:
                all_same = False

        if all_same:
            return True

        r += 1

    return False


def oldSlidingWindowTemplate(self, s1, s2):
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
