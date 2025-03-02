# @link - https://neetcode.io/problems/multiply-strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.solve(num1, num2)

    def solve(self, num1, num2):
        if '0' in [num1, num2]:
            return '0'

        ans = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(0, len(num1)):
            for j in range(0, len(num2)):
                pdt = int(num1[i]) * int(num2[j])
                ans[i + j + 1] += (ans[i + j] + pdt % 10) // 10 + pdt // 10
                ans[i + j] = (ans[i + j] + pdt % 10) % 10

        ans = ans[::-1]
        i = 0
        while i < len(ans):
            if ans[i] != 0:
                break
            i += 1

        return "".join(map(str, ans[i:]))