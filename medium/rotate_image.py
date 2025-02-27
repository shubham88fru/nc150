from typing import List

# @link - https://neetcode.io/problems/rotate-matrix
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.solve(matrix)

    def solve(self, matrix):
        self.tr(matrix)
        self.rr(matrix)

    def tr(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    def rr(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            l = 0
            r = n - 1

            while l < r:
                temp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = temp
                l += 1
                r -= 1