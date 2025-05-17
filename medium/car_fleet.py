from typing import List

""""""""""""""""""""""""""""
---------------------------------------------------------------
OPTIMAL: Sort (no need to use stack. see comments in java soln)
---------------------------------------------------------------
TC: O(nlog(n) + n) 
SC: O(n)

--------------------
BETTER: Sort + stack
--------------------
TC: O(nlog(n) + n) 
SC: O(n + fleet)

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/car-fleet
# @check - https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode
class Solution:

    # Had a hunch but couldn't solve on my own.
    # Solution based on explanation by nc.
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed), key=lambda pair: pair[0])

        stack = []
        for position, speed in sorted_pairs[::-1]:
            if len(stack) == 0:
                stack.append((target - position) / speed)
            else:
                curr_time = (target - position) / speed
                if curr_time > stack[-1]:
                    stack.append(curr_time)

        return len(stack)
