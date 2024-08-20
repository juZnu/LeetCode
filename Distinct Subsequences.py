def numDistinct( s, t):
    dp =[0 for _ in s]
    dp = dp+[0]
    for j in range(len(t)-1,-1,-1):
        for i in range(len(dp)-j,-1,-1):
            dp[i] = dp[i+1] + (1 if s[i] == t[j] else 0)
        

print(numDistinct(s = "rabbbit", t = "rabbit"))