from typing import List

from sortedcontainers import SortedDict

# @link - https://neetcode.io/problems/sliding-window-maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.solve(nums, k)

    # This is sliding window approach.
    # Albeit not optimal. Optimal approach
    # uses deque but will need to watch some
    # online soln for that.
    def solve(self, nums, k):
        n = len(nums)
        sd = SortedDict()
        ans = []
        l = 0
        r = 0

        while r < n:
            while r - l + 1 <= k:
                if nums[r] not in sd:
                    sd[nums[r]] = 0

                sd[nums[r]] += 1
                r += 1

            ans.append(sd.peekitem(-1)[0])
            rem = nums[l]
            sd[rem] -= 1
            if sd[rem] == 0:
                del sd[rem]
            l += 1

        return ans