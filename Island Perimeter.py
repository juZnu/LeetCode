from typing import List

def islandPerimeter( grid: List[List[int]]) -> int:
    visited = set()
    def solve(i,j):
        perimeter = 0 
        grid[i][j] = 0
        neighbours = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for a,b in neighbours:
            if not (0 <= a <len(grid) and 0 <= b <len(grid[0])):
                perimeter += 1
            elif grid[a][b] and (a,b) not in visited:
                visited.add((a,b))
                perimeter += solve(a,b)
            elif not grid[a][b] and (a,b) not in visited:
                perimeter += 1
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] :
                visited.add((i,j))
                return solve(i,j)
            
print(islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

