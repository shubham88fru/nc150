from typing import List

# @link - https://neetcode.io/problems/spiral-matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.solve(matrix)

    def solve(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        ans = []
        visited = [[0 for _ in range(n)] for _ in range(m)]
        ans.append(matrix[0][0])
        visited[0][0] = -1
        while (
                self.can_move(m, n, i, j + 1, visited) or
                self.can_move(m, n, i + 1, j, visited) or
                self.can_move(m, n, i, j - 1, visited) or
                self.can_move(m, n, i - 1, j, visited)
        ):

            while self.can_move(m, n, i, j + 1, visited):
                visited[i][j + 1] = -1
                ans.append(matrix[i][j + 1])
                j += 1

            while self.can_move(m, n, i + 1, j, visited):
                visited[i + 1][j] = -1
                ans.append(matrix[i + 1][j])
                i += 1

            while self.can_move(m, n, i, j - 1, visited):
                visited[i][j - 1] = -1
                ans.append(matrix[i][j - 1])
                j -= 1

            while self.can_move(m, n, i - 1, j, visited):
                visited[i - 1][j] = -1
                ans.append(matrix[i - 1][j])
                i -= 1

        return ans

    def can_move(self, m, n, i, j, visited):
        return i >= 0 and i < m and j >= 0 and j < n and visited[i][j] != -1