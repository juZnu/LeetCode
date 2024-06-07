import collections
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def bfs(i,j):
            grid[i][j] = 1
            queue = collections.deque()
            queue.append((i,j))
            while queue:
                r,c = queue.popleft()
                grid[r][c] = 1
                for dr,dc in directions:
                    ndr,ndc = r+dr,c+dc
                    if 0 <= ndr < len(grid) and 0 < ndc < len(grid[r]) and not grid[ndr][ndc]:
                        queue.append((ndr,ndc))
        
        for i in range(len(grid)):
            if not grid[i][0]:
                bfs(i,0)
            if not grid[i][len(grid[i])-1]:
                bfs(i,len(grid[i])-1)
        
        for i in range(len(grid[0])):
            if not grid[0][i]:
                bfs(0,i)
            if not grid[len(grid)-1][i]:
                bfs(len(grid)-1,i)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not grid[i][j]:
                    count+= 1
                    bfs(i,j)

        return count
            


