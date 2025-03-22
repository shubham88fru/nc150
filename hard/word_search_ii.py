from typing import List

# @link - https://neetcode.io/problems/search-for-word-ii
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return self.solve(board, words)

    def solve(self, board, words):
        root = self.insert_words_to_trie(words)

        m = len(board)
        n = len(board[0])

        ans = []
        for i in range(0, m):
            for j in range(0, n):
                self.search_and_add(board, i, j, root, ans)

        return ans

    def search_and_add(self, board, i, j, curr, ans):
        if curr.word != None:
            ans.append(curr.word)
            curr.word = None

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '.':
            return

        ch = board[i][j]
        if ch not in curr.node:
            return

        board[i][j] = '.'
        self.search_and_add(board, i + 1, j, curr.node[ch], ans)
        self.search_and_add(board, i - 1, j, curr.node[ch], ans)
        self.search_and_add(board, i, j + 1, curr.node[ch], ans)
        self.search_and_add(board, i, j - 1, curr.node[ch], ans)
        board[i][j] = ch

    def insert_words_to_trie(self, words):
        root = Trie()
        for word in words:
            self.insert(word, root)

        return root

    def insert(self, word, root):
        curr = root
        for i in range(0, len(word)):
            ch = word[i]
            if ch not in curr.node:
                new_node = Trie()
                new_node.ch = ch
                curr.node[ch] = new_node

            curr = curr.node[ch]
        curr.word = word


class Trie:
    def __init__(self):
        self.node = {}
        self.ch = ''
        self.word = None