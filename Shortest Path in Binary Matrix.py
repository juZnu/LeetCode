import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1

        directions =[(i,j) for i in [-1,0,1] for j in [-1,0,1] if  i or  j]
        visited = set()
        visited.add((0,0))
        queue = collections.deque()
        queue.append([0,0,1])

        while queue:

            row,col,length = queue.popleft()
            
            if row ==len(grid)-1 and col == len(grid[-1])-1:
                return length
            
            
            if max(row,col) >= len(grid) or min(row,col) < 0 or grid[row][col]:
                continue

            for i,j in directions:
            
                if (row+i,col+j) not in visited:
                    queue.append([row+i,col+j,length+1]) 
                    visited.add((row+i,col+j))
                    
        return -1