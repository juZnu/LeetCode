def hammingWeight( n):
    count = 0
    x = 2**0
    while n!=x:
        prev= n
        n = n & ~(n & x)
        count += 1 if prev != n else 0
        x *= 2
    return count +1

print(hammingWeight(11))