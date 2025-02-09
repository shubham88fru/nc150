from typing import List

# @link - https://neetcode.io/problems/search-2d-matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            j_ = mid % n
            i_ = mid // n

            curr = matrix[i_][j_]
            if curr == target:
                return True

            if curr > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

