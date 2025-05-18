from typing import List

""""""""""""""""""""""""""""
---------------------------------------
OPTIMAL: Binary search on entire matrix
---------------------------------------
TC: O(log(m*n))
SC: O(1)

--------------------------------
BETTER: Binary search row by row
--------------------------------
TC: O(m*log(n))
SC: O(1)

--------------------------------------------------------
ADDITIONAL: Start from top right and move to bottom left
--------------------------------------------------------
TC: O(m + n)
SC: O(1)

--------------------
BRUTE: linear search
--------------------
TC: O(m*n)
SC: O(1)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/search-2d-matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.revise(matrix, target)
        # return self.revise2(matrix, target)

    def revise(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    def revise2(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:  # need to increase - move down
                i += 1
            else:  # need to decrease - move left
                j -= 1

        return False

