from typing import List


def countSubIslands( grid1: List[List[int]], grid2: List[List[int]]) -> int:
    result = 0
    def isSubIsland(row,col):
        pass

    for row in range(len(grid2)):
        for col in range(len(grid2[row])):
            if grid2[row][col] and grid1[row][col]:
                result += 1 if isSubIsland(row,col) else 0
    return result
    
print(countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
        