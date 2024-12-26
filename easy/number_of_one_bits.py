
# @link - https://neetcode.io/problems/number-of-one-bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n & 1)
            n = n>>1

        return count