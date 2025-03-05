from typing import List

# @link - https://neetcode.io/problems/partition-equal-subset-sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.solve(nums)

    # This is a 2d dp approach which I
    # dont this is ideal. Redo during revision.
    def solve(self, nums):
        n = len(nums)

        total = sum(nums)
        if total % 2 != 0:
            return False

        return self.dp(nums, total / 2, 0, {})

    def dp(self, nums, target, i, cache):
        if target == 0:
            return True

        if i >= len(nums) or target < 0:
            return False

        k = str(i) + "_" + str(target)
        if k in cache:
            return cache[k]

        pick = self.dp(nums, target - nums[i], i + 1, cache)
        notPick = self.dp(nums, target, i + 1, cache)

        cache[k] = pick or notPick
        return cache[k]