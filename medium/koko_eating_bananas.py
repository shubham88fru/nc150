import math
from typing import List

""""""""""""""""""""""""""""
----------------------
OPTIMAL: Binary search
----------------------
TC: O(n + n*log(max(arr))
SC:

------------------------------------
BETTER:
------------------------------------
TC:
SC:

-----------------------------------------------------------------------------------------
BRUTE: Linear search. Start with 1 banana and see if possible, keep increasing one by one
-----------------------------------------------------------------------------------------
TC: O(n*max(arr)) ; where max(arr) is the maximum of the given piles.
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/eating-bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.bs(piles, h)

    # My soln. Binary search on answer pattern.
    def bs(self, piles, h):
        mx = max(piles)

        l = 1
        r = mx - 1

        ans = mx
        while l <= r:
            mid = l + (r - l) // 2
            hrs = self.eat(mid, piles)

            if hrs <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

    def eat(self, mid, piles):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / mid)

        return hrs

