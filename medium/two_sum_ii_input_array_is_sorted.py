from typing import List

""""""""""""""""""""""""""""
---------------------
OPTIMAL: Two pointers
---------------------
TC: O(n)
SC: O(1)

---------------
BETTER: Hashmap
---------------
TC: O(n)
SC: O(n)

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/two-integer-sum-ii
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    p1 = 0;
    p2 = len(numbers) - 1
    while p1 < p2:
        if numbers[p1] + numbers[p2] == target:
            return [p1 + 1, p2 + 1]

        if numbers[p1] + numbers[p2] < target:
            p1 += 1
        else:
            p2 -= 1

    return []