from typing import List

# @link - https://neetcode.io/problems/duplicate-integer
""""""""""""""""""""""""""""
----------------
OPTIMAL: Hashmap
----------------
TC: O(n)
SC: O(n)

------------------------------------
BETTER: Sort and compare neighbours.
------------------------------------
TC: O(n + nlog(n))
SC: O(1)

----------------------------------------------
BRUTE: For each check if exists anywhere else.
----------------------------------------------
TC: O(n^2)
SC: O(1)

"""""""""""""""""""""""""""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {};
        for num in nums:
            if num in dic:
                return True
            dic[num] = dic.get(num, 0) + 1
        return False