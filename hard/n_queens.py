from typing import List

# @link - https://neetcode.io/problems/n-queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.solve(n)

    def solve(self, n):
        ans = []
        board = []

        for i in range(n):
            board.append(['.'] * n)

        self.backtracking(n, 0, board, ans)

        return ans

    def backtracking(self, n, idx, board, ans):

        if idx >= n:
            lst = []
            for row in board:
                lst.append("".join(row))

            ans.append(lst)

            return

        for j in range(0, n):
            if self.canPlace(idx, j, n, board):
                board[idx][j] = 'Q'
                self.backtracking(n, idx + 1, board, ans)
                board[idx][j] = '.'

    def canPlace(self, i, j, n, board):
        return self.horiz(i, j, n, board) and self.verti(i, j, n, board) and self.fDiag(i, j, n, board) and self.bDiag(
            i, j, n, board)

    def horiz(self, i, j, n, board):
        for jj in range(n):
            if board[i][jj] == 'Q':
                return False
            jj += 1

        return True

    def verti(self, i, j, n, board):
        for ii in range(n):
            if board[ii][j] == 'Q':
                return False
            ii += 1

        return True

    def fDiag(self, i, j, n, board):
        jj = j + 1
        ii = i - 1
        while jj < n and ii >= 0:
            if board[ii][jj] == 'Q':
                return False
            jj += 1
            ii -= 1

        jj = j - 1
        ii = i + 1
        while ii < n and jj >= 0:
            if board[ii][jj] == 'Q':
                return False
            ii += 1
            jj -= 1

        return True

    def bDiag(self, i, j, n, board):
        jj = j + 1
        ii = i + 1
        while jj < n and ii < n:
            if board[ii][jj] == 'Q':
                return False
            jj += 1
            ii += 1

        jj = j - 1
        ii = i - 1
        while jj >= 0 and ii >= 0:
            if board[ii][jj] == 'Q':
                return False
            jj -= 1
            ii -= 1

        return True