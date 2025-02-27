# @link - https://neetcode.io/problems/pow-x-n
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.solve(x, n)

    # Optimal
    def solve(self, x, n):
        absn = abs(n)
        ans = 1.0
        while absn > 0:
            # 2^10 --> (2*2)^5
            if absn % 2 == 0:
                x = x * x
                absn //= 2
            else:
                # 4^5 --> 4 * (4)^4
                ans = ans * x
                absn -= 1

        return ans if n > 0 else 1 / ans

    # Brute force - using for loop.