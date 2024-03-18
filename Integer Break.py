def integerBreak( n: int) -> int:
    result = 0
    for i in range(1,n+1):
        result = max(result, i * integerBreak(n-i))
    return result 

print(integerBreak(2))