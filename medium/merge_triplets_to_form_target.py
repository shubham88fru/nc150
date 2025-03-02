from typing import List

# @link - https://neetcode.io/problems/merge-triplets-to-form-target
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        return self.solve(triplets, target)

    def solve(self, triplets, target):
        n = len(triplets)
        fFound = False
        sFound = False
        tFound = False

        for triplet in triplets:
            currF = triplet[0]
            currS = triplet[1]
            currT = triplet[2]

            if currF > target[0] or currS > target[1] or currT > target[2]:
                continue

            if currF == target[0]:
                fFound = True

            if currS == target[1]:
                sFound = True

            if currT == target[2]:
                tFound = True

            if fFound and sFound and tFound:
                return True

        return fFound and sFound and tFound