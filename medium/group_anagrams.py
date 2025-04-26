from typing import List

""""""""""""""""""""""""""""
-------------------------------------
OPTIMAL: 26 length freq array and map
-------------------------------------
TC: O(n*k + 26); k is length of longest string.
SC: O(anagrams)

---------------------------------------------------------
BETTER: sort each and create map for sorted v/s anagrams.
---------------------------------------------------------
TC: O(n*klog(k)) ; k is length of longest string.
SC: O(anagrams)

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/anagram-groups
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for st in strs:
            freq = [0] * 26
            for i in range(0, len(st)):
                ch = st[i];
                index = ord(ch) - ord('a')
                freq[index] += 1
            key = "_".join([str(f) for f in freq])

            if key not in freqs:
                freqs[key] = []
            freqs[key].append(st)

        return list(freqs.values())
