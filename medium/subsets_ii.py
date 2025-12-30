from typing import List

""""""""""""""""""""""""""""
-----------------
OPTIMAL: Good dfs
-----------------
TC: O(nlog(n) + n*2ˆn)
SC: O(n); recursive stack space.

------------------------------------
BETTER:
------------------------------------
TC:
SC:

------------------------------------------------
BRUTE: Pick-notPick patter with set and sorting.
------------------------------------------------
TC: O(nlog(n)*n*2ˆn); sorting each time we get a result.
SC: O(2n)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/subsets-ii
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.revise(nums)

    # Slight modification to appraoch 2 from subsets problem.
    # Approach 2 keeps the soln much more neater.
    # Check java repo for the nasty soln for this soln which
    # modifies approach 1 of the subsets problem to solve this q.
    def revise(self, candidates):
        n = len(candidates)
        ans = []
        self.backtrack2(n, sorted(candidates), 0, ans, [], set())
        return ans

    def backtrack2(self, n, candidates, idx, ans, sub, st):
        ans.append(sub[:])

        for i in range(idx, n):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue

            sub.append(candidates[i])
            self.backtrack2(n, candidates, i + 1, ans, sub, st)
            sub.pop()
