# @link - https://neetcode.io/problems/validate-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { '}': '{', ')': '(', ']': '[' };
        stack = []

        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            elif ch in pairs and stack[-1] != pairs[ch]:
                return False
            elif ch in pairs:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0