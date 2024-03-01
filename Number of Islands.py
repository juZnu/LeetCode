visited = set()
def BFS(i,j,grid):
    global visited
    neighbours = []
    if i+1 < len(grid) and (i+1,j) not in visited:
        neighbours.append((i+1,j))
    if j+1 < len(grid[0]) and (i,j+1) not in visited:
        neighbours.append((i,j+1))
    if i-1 > -1 and (i-1,j) not in visited:
        neighbours.append((i-1,j))
    if j-1 > -1 and (i,j-1) not in visited:
        neighbours.append((i,j-1))
    for ele in neighbours:

        if grid[ele[0]][ele[1]] == '1' and (ele not in visited):
            visited.add(ele)
            BFS(ele[0],ele[1],grid)

def numIslands(grid):
    count = 0
    global visited
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j] == '1' and (i,j) not in visited:
                visited.add((i,j))
                count +=1
                BFS(i,j,grid)
    return count
        
print(numIslands(grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

print('0'==True)