from typing import List


def minFallingPathSum( grid: List[List[int]]) -> int:
    
    for index in range(len(grid)-2,-1,-1):
        sorted_array = sorted(grid[index+1])
        for j in range(len(grid[index])):
            grid[index][j] += sorted_array[0] if grid[index+1][j] !=  sorted_array[0] else sorted_array[1]

    return min(grid[0])

print(minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]))