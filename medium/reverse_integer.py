import math

# @link - https://neetcode.io/problems/reverse-integer
class Solution:
    def reverse(self, x: int) -> int:
        return self.solve(x)

    # Based on NC's approach
    def solve(self, x):
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or
                    (res == MAX // 10 and digit >= MAX % 10)):
                return 0

            if (res < MIN // 10 or
                    (res == MIN // 10 and digit <= MIN % 10)):
                return 0

            res = (res * 10) + digit

        return res