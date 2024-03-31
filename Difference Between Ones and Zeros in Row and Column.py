from typing import List


def onesMinusZeros( grid: List[List[int]]) -> List[List[int]]:
    result  = []
    for i in grid:
        x = sum(i)
        result.append([2*x - len(i) for _  in range(len(i))])
    for i in range(len(grid[0])):
        x = sum([row[i] for row in grid])
        for j in range(len(result)):
            result[j][i] += 2*x - len(grid)
    return result

print(onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))