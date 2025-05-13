""""""""""""""""""""""""""""
----------------
OPTIMAL: Stacks
----------------
TC: O(1)
SC: O(n)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/minimum-stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 2 ** 63

    def push(self, val: int) -> None:
        if val < self.mini:
            self.mini = val

        self.stack.append([val, self.mini])

    def pop(self) -> None:
        pair = self.stack.pop()

        if len(self.stack) == 0:
            self.mini = 2 ** 63
        else:
            self.mini = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.mini

