# @link - https://neetcode.io/problems/interleaving-string
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.solve(s1, s2, s3)

    # Directly writing the optimal to-down soln.
    # check java for my og suboptimal soln based
    # on my initial intuition that gave TLE.
    def solve(self, s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1+n2 != n3:
            return False

        memo = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

        return self.dp(s1, s2, s3, 0, 0, memo)

    def dp(self, s1, s2, s3, i, j, memo):
        if i + j >= len(s1) + len(s2):
            return True

        # In this implementation, i+j is
        # guaranteed to be less than len(s3)
        # coz we have ensured that len(s1) + len(s2) == len(s3)
        # and we call recursive functions below only when i and j
        # are in their bounds.
        ch = s3[i+j]

        if memo[i][j] != -1:
            return memo[i][j]

        one = False
        if i < len(s1) and s1[i] == ch:
            one =  self.dp(s1, s2, s3, i+1, j, memo)

        two = False
        if (j < len(s2) and s2[j] == ch):
            two = self.dp(s1, s2, s3, i, j+1, memo)

        memo[i][j] = one or two
        return one or two