
# @link - https://neetcode.io/problems/design-word-search-data-structure
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(0, len(word)):
            ch = word[i]
            if ch not in curr.node:
                curr.node[ch] = TrieNode()

            curr = curr.node[ch]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.searchRecursive(word, 0, self.root)

    def searchRecursive(self, word, idx, root):
        if root is None:
            return False

        if idx >= len(word) and root.endOfWord:
            return True

        if idx >= len(word):
            return False

        ch = word[idx]
        if (ch != '.' and ch not in root.node):
            return False

        matched = False
        wildcard = False
        if ch == '.':
            for key in root.node:
                wildcard = self.searchRecursive(word, idx + 1, root.node[key])
                if wildcard:
                    break
        else:
            matched = self.searchRecursive(word, idx + 1, root.node[ch])

        return matched or wildcard


class TrieNode:
    def __init__(self):
        self.ch = ''
        self.node = {}
        self.endOfWord = False