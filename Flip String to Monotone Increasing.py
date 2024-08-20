class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp =[float('inf') for _ in range(len(s)+1)]
        dp[0] = 0
        
        for ele in '10':
            for i in range(1,len(s)+1):
                dp[i] = min(dp[i],dp[i-1] +(1 if s[i-1] ==ele else 0))

        return dp[-1]
            



        