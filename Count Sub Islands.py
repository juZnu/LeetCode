class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        grid = [[ 1 if grid1[m][n] and grid2[m][n] else 0 for n in range(len(grid1[m]))] for m in range(len(grid1))]

        res = 0
        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        def dfs(i,j):
            grid2[i][j] = 0

            res = True if grid1[i][j] else False
            for dx,dy in directions:
                if (0 <= i+dx < len(grid) and 0 <= j+dy < len(grid2[i])) and grid2[i+dx][j+dy]:
                   res &= dfs(i+dx,j+dy)
            return res

        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if grid2[i][j]:
                    res += 1 if dfs(i,j) else 0
        
        return res
