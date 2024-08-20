from typing import List


def coinChange( coins: List[int], amount: int) -> int:
    coins.sort()
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for change in range(coin,len(dp)):
            dp[change] = min(1+dp[change-coin], dp[change])

    return dp[-1] if dp[-1] != float('inf') else -1

    
   

print(coinChange(coins = [1,2,5], amount = 11))
    