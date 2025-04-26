from typing import List

""""""""""""""""""""""""""""
--------------------------------------------------------------
FOLLOWUP: Not allowed to use map --> sort and use two pointers
--------------------------------------------------------------
TC: O(nlogn + n) if array not sorted already, else O(n) 
SC: O(1)

--------------------------
OPTIMAL: One pass with map
--------------------------
TC: O(n)
SC: O(n)

-------------------------------------------------------------------
BETTER: 2 pass. store all nums first, then second pass to find pair
-------------------------------------------------------------------
TC: O(n + n)
SC: O(n)

----------------------------------------------------------
BRUTE: For each, sum with other and see if adds to target.
----------------------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/two-integer-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            pair = target - num
            if pair in dic:
                return sorted([idx, dic.get(pair)])
            dic[num] = idx

        return [-1, -1]