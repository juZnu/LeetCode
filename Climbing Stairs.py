class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        count = [0 for  _ in range(n)]
        def dfs(i,count):
            if i == n:
                return 1
            elif i > n:
                return 0
            if count[i-1]:
                count[-1] += count[i-1]
                return count[i-1]
            count[i-1] = dfs(i+1,count)+dfs(i+2,count)
            count[-1] += count[i-1]
            return count[i-1]
        dfs(1,count) 
        return count[0]+count[1]
            