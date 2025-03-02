# @link - https://neetcode.io/problems/sum-of-two-integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return self.solve(a, b)

    # coded based on explanation by nc.
    # Python integers are arbitrarily long
    # and so, this approach isn't suitable for
    # python. Even nc did in java.
    def solve(self, a, b):
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a