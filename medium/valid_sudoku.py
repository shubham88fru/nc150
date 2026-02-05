from typing import List

""""""""""""""""""""""""""""
----------------------------
OPTIMAL: Hashmap and HashSet
----------------------------
TC: O(n^2)
SC: O(n^2)

------------------------------------
BETTER: didn't find.
------------------------------------
TC:
SC:

-------------------------------------------------
BRUTE: Separate loops for each row, col and boxes 
-------------------------------------------------
TC: O(n^2 + nˆ2 + nˆ2)
SC: O(n^2)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        cells = {}

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch == '.':
                    continue

                if i not in rows:
                    rows[i] = set()
                if ch in rows[i]:
                    return False
                rows[i].add(ch)

                if j not in cols:
                    cols[j] = set()
                if ch in cols[j]:
                    return False
                cols[j].add(ch)

                str_key = str(i // 3) + str(j // 3)
                if str_key not in cells:
                    cells[str_key] = set()
                if ch in cells[str_key]:
                    return False
                cells[str_key].add(ch)

        return True