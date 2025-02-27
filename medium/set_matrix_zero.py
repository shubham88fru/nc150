from typing import List

# @link - https://neetcode.io/problems/set-zeroes-in-matrix
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.solve(matrix)

    # 1) This is the most optimal
    # approach. TC: O(m*n) and SC: O(1)
    def solve(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        col_0_has_zero = 1
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col_0_has_zero = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0

        if col_0_has_zero == 0:
            for i in range(0, m):  # careful
                matrix[i][0] = 0

    # 2) A better (but suboptimal) approach
    # is to take two extra arrays of size m and n
    # if a 0 is present in a cell, mark corresonding
    # indexes in the arrays to replace entire row and
    # col to zero.

    # 3) A brute forcish appraoch is to take a complete
    # new matrix. Iterate the og matrix, if its 1, put 1
    # in the new matrix and if its 0, set corresponding rows
    # cols of the new matrix to 0.