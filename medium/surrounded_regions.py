from typing import List

# @link - https://neetcode.io/problems/surrounded-regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.nasty_brute_force(board)

    def nasty_brute_force(self, board):
        m = len(board)
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'O':
                    visited = [[0 for _ in range(n)] for _ in range(m)]
                    edge = [False]
                    lst = []
                    self.check(board, visited, edge, i, j, lst)
                    if (edge[0] == False):
                        for k in range(0, len(lst)):
                            board[lst[k][0]][lst[k][1]] = 'X'

    def check(self, board, visited, edge, i, j, lst):
        if i < 0 or i >= len(board):
            edge[0] = True
            return

        if j < 0 or j >= len(board[0]):
            edge[0] = True
            return

        if visited[i][j] == -1:
            return

        if board[i][j] == 'X':
            return

        visited[i][j] = -1
        lst.append([i, j])
        self.check(board, visited, edge, i, j - 1, lst)
        self.check(board, visited, edge, i, j + 1, lst)
        self.check(board, visited, edge, i - 1, j, lst)
        self.check(board, visited, edge, i + 1, j, lst)