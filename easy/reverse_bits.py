# @link - https://neetcode.io/problems/reverse-bits
class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = ""
        i = 0
        while i < 32:
            bit_str += str(n & 1)
            n = n >> 1
            i += 1

        return int(bit_str, 2)