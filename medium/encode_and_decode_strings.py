from typing import List

# @link - https://neetcode.io/problems/string-encode-and-decode
class Solution:

    def encode(self, strs: List[str]) -> str:
        ser = ""
        for st in strs:
            ser += (str(len(st)) + "#" + st)

        return ser

    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)

        i = 0
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1
            lt = int(s[i:j])
            ans.append(s[j + 1: j + 1 + lt])
            i = j + 1 + lt

        return ans