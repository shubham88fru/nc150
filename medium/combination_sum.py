from typing import List

""""""""""""""""""""""""""""
------------------------
OPTIMAL: binary tree dfs
------------------------
TC: O(n*2ˆt); where `t` is the target.
SC: O(t); max depth of recursive stack space.

-----------------------
BETTER: 
-----------------------
TC:
SC:

---------------------
BRUTE: n-ary tree dfs
---------------------
TC: O(n*nˆt) = O(nˆ(t+1)); where `t` is the target
SC: O(t); max depth of recursive stack space.

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/combination-target-sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.revise(candidates, target)

    def revise(self, candidates, target):
        ans = []
        self.backtrack2(candidates, target, 0, ans, [])
        # self.backtrack1(candidates, target, 0, ans, [])
        return ans

    # Similar to subsets problem, use this style of
    # writing code (instead of pick/notpick style), this
    # will lead to cleaner code when the array has duplicates.
    # This is basically n-ary tree traversal, cause we have
    # worst case n options each time.
    def backtrack2(self, candidates, target, idx, ans, sub):
        if target == 0:
            ans.append(sub[:])
            return

        if target < 0:
            return

        for i in range(idx, len(candidates)):
            sub.append(candidates[i])
            self.backtrack2(candidates, target - candidates[i], i, ans, sub)
            sub.pop()

    # This is binary tree traversal basically.
    # we have 2 options each time.
    def backtrack1(self, candidates, target, i, ans, sub):
        if target == 0:
            ans.append(sub[:])
            return

        if i >= len(candidates):
            return

        if target < 0:
            return

        sub.append(candidates[i])
        self.backtrack1(candidates, target - candidates[i], i, ans, sub)
        sub.pop()

        self.backtrack1(candidates, target, i + 1, ans, sub)