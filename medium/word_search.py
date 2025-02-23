from typing import List

# @link - https://neetcode.io/problems/search-for-word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.solve(board, word)

    def solve(self, board, word):
        m = len(board)
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                visited = [[0 for _ in range(n)] for _ in range(m)]
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, m, n, visited):
                        return True

        return False

    def dfs(self, board, word, wi, i, j, m, n, visited):
        if wi >= len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] != 0 or board[i][j] != word[wi]:
            return False

        visited[i][j] = -1

        up = self.dfs(board, word, wi + 1, i - 1, j, m, n, visited)
        right = self.dfs(board, word, wi + 1, i, j + 1, m, n, visited)
        down = self.dfs(board, word, wi + 1, i + 1, j, m, n, visited)
        left = self.dfs(board, word, wi + 1, i, j - 1, m, n, visited)

        visited[i][j] = 0

        return up or left or right or down