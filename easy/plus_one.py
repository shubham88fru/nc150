from typing import List

# @link - https://neetcode.io/problems/plus-one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for idx, dig in enumerate(reversed(digits)):
            rev_idx = len(digits) - 1 - idx  # idx will 0, 1, 2 .. only. Need to conv.
            new_dig = carry + dig
            if new_dig > 9:
                new_dig %= 10
                carry = 1
            else:
                carry = 0

            digits[rev_idx] = new_dig

        if carry == 1:
            digits.insert(0, 1)

        return digits