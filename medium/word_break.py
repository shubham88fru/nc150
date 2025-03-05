from typing import List

# @link - https://neetcode.io/problems/word-break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.solve(s, wordDict)

    def solve(self, s, wordDict):
        st = set(wordDict)

        return self.dp(s, st, {})

    def dp(self, s, wordDict, memo):
        if s in wordDict:
            return True

        if s in memo:
            return memo[s]

        for i in range(0, len(s)):
            sub = s[0: i + 1]
            if sub in wordDict:
                if self.dp(s[i + 1::], wordDict, memo):
                    memo[s] = True
                    return memo[s]

        memo[s] = False
        return memo[s]