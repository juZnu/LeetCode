class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        carry = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]


        for j in range(len(grid[0])-2,-1,-1):
            for i in range(len(grid)):
                num1 = carry[i-1][j+1] if (i-1 >=0 and grid[i][j] < grid[i-1][j+1]) else  0
                num2 = carry[i][j+1] if grid[i][j] < grid[i][j+1] else 0
                num3 = carry[i+1][j+1] if (i+1 <len(grid) and grid[i][j] < grid[i+1][j+1]) else  0
                carry[i][j] += max(num1,num2,num3)

        res = 0
        for i in range(len(grid)):
            res = max(res,carry[i][0])
        
        return res - (1 if res else 0)



      