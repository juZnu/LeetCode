def climbStairs( n):
    n2,n3 = 1,1
    for i in range(2,n+1):
        temp  = n2+n3
        n2 = n3
        n3 = temp
    return n3

print(climbStairs(4))