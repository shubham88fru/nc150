from typing import List

""""""""""""""""""""""""""""
------------
OPTIMAL: DFS
------------
TC: O(m*n*4ˆL); where L is the length of the word to be searched.
SC: O(L); recursive stack space will be at most length of the word.

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------
BRUTE: 
----------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/search-for-word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.revise(board, word)

    def revise(self, board, word):
        m = len(board)
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0, m, n):
                    return True

        return False

    def dfs(self, board, word, i, j, k, m, n):
        if k >= len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or word[k] != board[i][j] or board[i][j] == '#':
            return False

        og = board[i][j]
        board[i][j] = '#'
        up = self.dfs(board, word, i - 1, j, k + 1, m, n)
        right = self.dfs(board, word, i, j + 1, k + 1, m, n)
        down = self.dfs(board, word, i + 1, j, k + 1, m, n)
        left = self.dfs(board, word, i, j - 1, k + 1, m, n)
        board[i][j] = og

        return up or right or down or left