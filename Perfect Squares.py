class Solution(object):
    def numSquares(self, n):
        if math.sqrt(n)%1 ==0:return 1
        
        dp = [ float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            if math.sqrt(i)%1 ==0:
                for j in range(i,n+1):        
                    dp[j] = min(dp[j], 1 + dp[j-i])
            
        return dp[-1]

        
        