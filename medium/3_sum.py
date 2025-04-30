from typing import List

""""""""""""""""""""""""""""
-------------------
OPTIMAL: 3 pointers
-------------------
TC: O(n^2 + nlog(n))
SC: O(1)

-------------------------
BETTER: 2 loops and 2 sum
-------------------------
TC: O(n^2)
SC: O(n)

------------------
BRUTE: 3 for loops
------------------
TC: O(n^3)
SC: O(num of triplets)

"""""""""""""""""""""""""""
# @link - https://neetcode.io/problems/three-integer-sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return self.sol2(nums)
        return self.sol1(nums)

    # Optimal
    def sol1(self, nums):
        nums.sort()
        ans = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return ans

    # Suboptimal
    def sol2(self, nums):
        st = set()
        ans = []
        for i in range(0, len(nums) - 2):
            st2 = set()
            for j in range(i + 1, len(nums)):
                tg = -(nums[i] + nums[j])

                if tg in st2:
                    triplet = [nums[i], nums[j], tg]
                    triplet.sort()
                    if "_".join(map(str, triplet)) not in st:
                        ans.append(triplet)
                        st.add("_".join(map(str, triplet)))
                else:
                    st2.add(nums[j])

        return ans