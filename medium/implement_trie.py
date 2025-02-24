# @link - https://neetcode.io/problems/implement-prefix-tree
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(0, len(word)):
            ch = word[i]
            if ch not in curr.node:
                curr.node[ch] = TrieNode()

            curr = curr.node[ch]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(0, len(word)):
            ch = word[i]
            if ch not in curr.node:
                return False

            curr = curr.node[ch]

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(0, len(prefix)):
            ch = prefix[i]
            if ch not in curr.node:
                return False

            curr = curr.node[ch]

        return True


class TrieNode:
    def __init__(self):
        self.ch = ''
        self.node = {}
        self.endOfWord = False