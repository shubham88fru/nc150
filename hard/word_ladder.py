from collections import defaultdict, deque
from typing import List

# @Link - https://neetcode.io/problems/word-ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.solve(beginWord, endWord, wordList)

    # 1) Edctv's soln is optimal (ig)

    # 2) Suboptimal but intuitive to me.
    def solve(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        graph = defaultdict(list)

        for i in range(0, len(wordList)):
            for j in range(i + 1, len(wordList)):
                word1 = wordList[i]
                word2 = wordList[j]
                if self.diff(word1, word2) == 1:
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        if endWord not in graph:
            return 0

        q = deque()
        q.append([beginWord, 0])
        visited = set()
        visited.add(beginWord)

        while q:
            pair = q.popleft()

            if pair[0] == endWord:
                return pair[1] + 1

            visited.add(pair[0])
            ngs = graph[pair[0]]

            for ng in ngs:
                if ng not in visited:
                    q.append([ng, pair[1] + 1])

        return 0

    def diff(self, word1, word2):
        n = len(word1)

        j = 0
        dc = 0
        while j < n:
            if word1[j] != word2[j]:
                dc += 1
            if dc > 1:
                break
            j += 1
        return dc