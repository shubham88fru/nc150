from typing import List

# @lin - https://neetcode.io/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return self.solve(gas, cost)

    # Neither mik nor nc were very sure
    # why greedy works, specifically the
    # second part. If this problem comes in
    # in the interview, start with brute force
    # (check a loop from each index).
    def solve(self, gas, cost):
        n = len(gas)

        tg = sum(gas)
        tc = sum(cost)

        if tg < tc:
            return -1

        si = 0
        net = 0
        for i in range(0, n):
            net += (gas[i] - cost[i])
            if net < 0:
                net = 0
                si = i + 1

        return si