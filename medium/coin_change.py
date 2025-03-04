from typing import List

# @link - https://neetcode.io/problems/coin-change
def coinChange(self, coins: List[int], amount: int) -> int:
    ans = self.solve(coins, amount)
    return -1 if ans == pow(2, 31) * 10000 else ans


def solve(self, coins, amount):
    return self.dp(coins, amount, 0, {})


def dp(self, coins, amount, idx, memo):
    if amount == 0:
        return 0

    if amount < 0:
        return pow(2, 31) * 10000

    if idx >= len(coins):
        return pow(2, 31) * 10000

    k = str(amount) + "_" + str(idx)
    if k in memo:
        return memo[k]

    pick = 1 + self.dp(coins, amount - coins[idx], idx, memo)
    notPick = self.dp(coins, amount, idx + 1, memo)

    memo[k] = min(pick, notPick)
    return memo[k]