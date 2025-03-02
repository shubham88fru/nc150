from typing import List

# @link - https://neetcode.io/problems/partition-labels
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return self.solve(s)

    def solve(self, s):
        n = len(s)

        mp = {}
        for i in range(0, n):
            mp[s[i]] = i

        si = 0
        ei = 0
        ans = []
        for i in range(0, n):
            ei = max(ei, mp[s[i]])
            if i == ei:  # no char in curr partition extends beyond this.
                ans.append(ei - si + 1)
                si = i + 1
                ei = 0

        return ans