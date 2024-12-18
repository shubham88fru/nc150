from typing import List

# @link - https://neetcode.io/problems/two-integer-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            pair = target - num
            if pair in dic:
                return sorted([idx, dic.get(pair)])
            dic[num] = idx

        return [-1, -1]