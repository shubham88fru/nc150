# @link - https://neetcode.io/problems/non-cyclical-number
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        nn = n
        while True:
            sq_sum = 0
            while nn > 0:
                dig = nn%10
                sq_sum += (dig**2)
                nn = nn//10
            if sq_sum == 1:
                return True
            elif sq_sum in cache:
                return False

            nn = sq_sum
            cache.add(sq_sum)
        return False