from typing import List

# @link - https://neetcode.io/problems/evaluate-reverse-polish-notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+", "-", "*", "/"])
        stack = [tokens[0]]
        res = 0
        for i in range(1, len(tokens)):
            token = tokens[i]
            if token in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = self.operate(num1, num2, token)
                print(num1, num2, token, res)
                stack.append(res)

            else:
                stack.append(token)

        return int(stack.pop())

    def operate(self, num1, num2, token):
        match token:
            case "+":
                return num1 + num2
            case "-":
                return num2 - num1
            case "*":
                return num1 * num2
            case "/":
                return num2 / num1