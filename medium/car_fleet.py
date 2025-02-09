from typing import List

# @link - https://neetcode.io/problems/car-fleet
class Solution:
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
