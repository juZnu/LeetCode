def arrangeCoins( n: int) -> int:
    if n==1: return 1
    count = 0
    carry = 0
    while n> 0:
        carry += 1
        n -= carry
        count += 1
    return count - (1 if n else 0 )

print(arrangeCoins(3))