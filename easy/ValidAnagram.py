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
