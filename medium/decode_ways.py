# @link - https://neetcode.io/problems/decode-ways
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.solve(s)

    def solve(self, s):
        st = set()
        for i in range(1, 27):
            st.add(str(i))

        return self.dp(s, st, {})

    def dp(self, s, st, memo):
        if len(s) == 0:
            return 1

        if s in memo:
            return memo[s]

        count = 0
        for i in range(0, len(s)):
            left_sub = s[0: i + 1]
            if left_sub in st:
                count += self.dp(s[i + 1::], st, memo)
            else:
                break

        memo[s] = count
        return memo[s]