class Solution:
    def numTrees(self, n: int) -> int:
        memo={0:1,1:1,2:2}
        for i in range(n+1):
            if i in memo:
                continue
            count = 0
            for j in range(i):
                count += memo[j] * memo[i-1-j]

            memo[i] = count
        
        return memo[n]




            
        