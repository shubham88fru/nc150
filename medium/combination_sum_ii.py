from typing import List

# @link - https://neetcode.io/problems/combination-target-sum-ii
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solve(candidates, target)

    # This problem also has duplicates and so
    # its benificial to use the better approach of
    # subsets problem.
    # Trying to solve it using the 01 knapsack way
    # would make the solution complicated
    # and nasty.
    def solve(self, candidates, target):
        ans = []
        candidates.sort()
        self.backtrack(candidates, target, ans, 0, [])

        return ans;

    def backtrack(self, candidates, target, ans, idx, curr):
        if target == 0:
            ans.append(list(curr))
            return

        # subsets
        for i in range(idx, len(candidates)):
            if i != idx and candidates[i] == candidates[i - 1]:
                continue

            if target - candidates[i] >= 0:
                curr.append(candidates[i])
                self.backtrack(candidates, target - candidates[i], ans, i + 1, curr)
                curr.pop()
