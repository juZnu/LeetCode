def isThereAPath(grid):
    grid =[[j if i else -1 for j in grid[i]] for i in range(len(grid))]
    def dfs(i,j,sum_):
        if i == len(grid)-1 and j == len(grid[-1])-1:
            sum_ += grid[-1][-1]
            return not sum_
        elif 0 <= i < len(grid) and 0 <= j < len(grid[0]): 
            return dfs(i+1,j, sum_+grid[i][j]) or dfs(i,j+1,sum_+grid[i][j])
        else:
            return False
    return dfs(0,0,0)
        

print(isThereAPath(grid = [[1,1,0],[0,0,1],[1,0,0]]))
        