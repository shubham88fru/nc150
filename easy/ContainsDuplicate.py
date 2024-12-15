from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {};
        for num in nums:
            if num in dic:
                return True
            dic[num] = dic.get(num, 0) + 1
        return False