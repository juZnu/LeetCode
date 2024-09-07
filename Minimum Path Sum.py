class Solution(object):
    def minPathSum(self, grid):
        m , n = len(grid) , len(grid[0])
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(n):
                ele1 = grid[i-1][j]
                ele2 = grid[i][j-1] if j else float('inf')
                grid[i][j] += min(ele1,ele2)
        
        return grid[-1][-1]


        