from typing import List

# @link - https://neetcode.io/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.solve(nums)

    # Slight modification to appraoch 2 from subsets problem.
    # Approach 2 keeps the soln much more neater.
    # Check java repo for the nasty soln for this soln which
    # modifies approach 1 of the subsets problem to solve this q.
    def solve(self, nums):
        nums.sort()  # extra step
        ans = []
        self.bactrack2(nums, 0, ans, [])
        return ans

    def bactrack2(self, nums, idx, ans, curr):
        ans.append(list(curr))

        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i - 1]:  # extra step
                continue

            curr.append(nums[i])
            self.bactrack2(nums, i + 1, ans, curr)
            curr.pop()
