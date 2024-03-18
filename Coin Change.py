from typing import List


def coinChange( coins: List[int], amount: int) -> int:
    coins.sort()
    result  = 0
    while amount > 0 :
        coin = coins.pop()
        result += amount// coin
        amount %= coin
    return -1 if amount else result

print(coinChange(coins = [186,419,83,408], amount = 6249))
    