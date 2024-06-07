import collections


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def dfs(i,j):
            grid[i][j] = 0
            queue = collections.deque()
            queue.append((i,j))

            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    rdr = r+dr
                    cdc = c+dc
                    if 0 <= rdr < len(grid) and 0 <= cdc < len(grid[i]) and grid[rdr][cdc]:
                        grid[rdr][cdc] = 0
                        queue.append((rdr,cdc))
        
        for i in range(len(grid[0])):
            if grid[0][i]:
                dfs(0,i)
            if grid[len(grid)-1][i]:
                dfs(len(grid)-1,i)

        for i in range(1,len(grid)-1):
            if grid[i][0]:
                dfs(i,0)
            if grid[i][len(grid[i])-1]:
                dfs(i,len(grid[i])-1)
                    
                    
        return sum([sum(grid[i]) for i in range(len(grid))])

        