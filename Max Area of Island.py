from typing import List


def maxAreaOfIsland( grid: List[List[int]]) -> int:
    area = 0
    def dfs(grid,row,col):
        result = 0
        directions = [(row-1,col),(row+1,col),(row,col+1),(row,col-1)]
        for r,c in directions:
            if  0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
                grid[r][c] = 0
                result += 1 + dfs(grid,r,c) 
        return result
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                grid[row][col] = 0
                area = max(area,1 + dfs(grid,row,col))
    return area

print(maxAreaOfIsland(grid = [[1,1]]))