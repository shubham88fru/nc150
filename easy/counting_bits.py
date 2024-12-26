from typing import List

# @link - https://neetcode.io/problems/counting-bits
class Solution:

    # Following is a brute force solution.
    # @check dsalgo for dp solution.
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(self.countOnes(i))

        return ans

    def countOnes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n & 1)
            n = n >> 1

        return count