from typing import List


def coinChange( coins: List[int], amount: int) -> int:
    coins.sort()
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i-coin] + 1, dp[i])
    return dp[-1]

print(coinChange(coins = [1,2,5], amount = 11))
    