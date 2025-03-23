from typing import List

# @link - https://neetcode.io/problems/foreign-dictionary
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        return self.solve(words)

    def solve(self, words):
        graph = {}
        indeg = {}

        for word in words:
            for ch in word:
                indeg[ch] = 0

        n = len(words)
        for i in range(0, n - 1):
            # Not sure why only taking
            # adjacent words works. My thinking
            # is that each preceding word
            # should be matched with each
            # subsequent word.
            word1 = words[i]
            word2 = words[i + 1]

            n1 = len(word1)
            n2 = len(word2)

            j = 0
            while j < n1 and j < n2:
                ch1 = word1[j]
                ch2 = word2[j]

                if ch1 != ch2:
                    if ch1 not in graph:
                        graph[ch1] = []

                    alreadyPresent = False
                    for ch in graph[ch1]:
                        if ch == ch2:
                            alreadyPresent = True
                            break

                    if alreadyPresent == False:
                        graph[ch1].append(ch2)
                        indeg[ch2] += 1
                    break

                j += 1

            # word2 is a prefix but comes later.
            if j >= n1 or j >= n2:
                if len(word2) < len(word1):
                    return ""

        ans = ""
        visited = 0
        q = deque()

        for ch in indeg:
            if indeg[ch] == 0:
                q.append(ch)

        while q:
            ch = q.popleft()
            ans += ch
            visited += 1

            if ch not in graph:
                continue

            for ng in graph[ch]:
                indeg[ng] -= 1
                if indeg[ng] == 0:
                    q.append(ng)

        return "" if visited < len(indeg) else ans