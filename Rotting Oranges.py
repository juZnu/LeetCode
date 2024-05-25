from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append([i,j])
                    
        count = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while rotten:
            carry = []
            for row ,col in rotten:
                for dr,dc in directions:
                    cdc = col + dc
                    rdr = row + dr
                    
                    if 0 <= rdr < len(grid) and 0 <= cdc< len(grid[row]) and grid[rdr][cdc] == 1:
                        grid[rdr][cdc] = 2
                        carry.append([rdr,cdc])
                        
            count += 1 if carry else 0
            rotten = carry
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 :
                    return -1
        
        return count