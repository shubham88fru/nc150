from typing import List

""""""""""""""""""""""""""""
--------------------------------------
OPTIMAL: Sort first and then recursion
--------------------------------------
TC: O(nlog(n) + n*2ˆn)
SC: O(n)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

-------------------------------------------------
BRUTE: Recursion and Sorting to remove duplicates
-------------------------------------------------
TC: O(nlog(n)*2ˆn)
SC: O(2n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/combination-target-sum-ii
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.revise(candidates, target)

    # This problem also has duplicates and so
    # it's beneficial to use the better approach of
    # subsets problem.
    # Trying to solve it using the 01 knapsack way
    # would make the solution complicated
    # and nasty.
    def revise(self, candidates, target):
        n = len(candidates)
        ans = []
        # self.backtrack1(n, candidates, target, 0, ans, [], set())
        self.backtrack2(n, sorted(candidates), target, 0, ans, [], set())
        return ans

    def backtrack2(self, n, candidates, target, idx, ans, sub, st):
        if target == 0:
            ans.append(sub[:])
            return

        if idx >= n:
            return

        for i in range(idx, n):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            sub.append(candidates[i])
            self.backtrack2(n, candidates, target - candidates[i], i + 1, ans, sub, st)
            sub.pop()

    def backtrack1(self, n, candidates, target, i, ans, sub, st):
        if target == 0:
            sorted_lst = "_".join(map(str, sorted(sub)))
            if sorted_lst not in st:
                ans.append(sub[:])
                st.add(sorted_lst)
            return

        if i >= n:
            return

        sub.append(candidates[i])
        self.backtrack1(n, candidates, target - candidates[i], i + 1, ans, sub, st)
        sub.pop()

        self.backtrack1(n, candidates, target, i + 1, ans, sub, st)