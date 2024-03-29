from typing import List

def islandPerimeter( grid: List[List[int]]) -> int:
    visitedOne = set()
    def helper(row,col):
        result = 0
        directions = [(row-1,col),(row,col-1),(row+1,col),(row,col+1)]
        for row,col in directions:
            if 0<= row < len(grid) and 0<= col < len(grid[0]) and grid[row][col] :
                if not (row,col) in visitedOne:
                    visitedOne.add((row,col))
                    result += helper(row,col)
            else:
                result+= 1
        return result
  
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                visitedOne.add((row,col))
                return 1+helper(row,col)-1
            
print(islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

