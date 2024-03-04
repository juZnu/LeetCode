class Solution(object):
    def DFS(self,i,j,grid):
        neighbours = []
        if i+1 < len(grid):
            neighbours.append((i+1,j))
        if j+1 < len(grid[0]):
            neighbours.append((i,j+1))
        if i-1 > -1:
            neighbours.append((i-1,j))
        if j-1 > -1:
            neighbours.append((i,j-1))
        for ele in neighbours:
            if grid[ele[0]][ele[1]] == '1':
                grid[ele[0]][ele[1]] ='0'
                self.DFS(ele[0],ele[1],grid)
        
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' :
                    grid[i][j] = '0'
                    count +=1
                    self.DFS(i,j,grid)
        return count
        
obj = Solution()       
print(obj.numIslands(grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

