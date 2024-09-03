class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        beginSet, endSet = set(), set()
        copyGrid = grid.copy()
        n, island= len(grid), 0
        dist = 0
        directions =[(-1,0),(0,-1),(1,0),(0,1)]

        def island_coord(i,j,visited):
            copyGrid[i][j] = 0
            visited.add((i,j))
            for dx,dy in directions:
                new_i,new_j = i+dx,j+dy
                if 0 <= new_i < n and 0 <= new_j < n and (new_i,new_j) not in visited:
                    if copyGrid[new_i][new_j]:island_coord(new_i,new_j,visited)
        

        for i in range(n):
            for j in range(n):
                if copyGrid[i][j]:
                    island_coord(i,j, endSet if island else beginSet)
                    island += 1
            if island == 2:
                break
        
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            dist += 1
            newSet =set()

            for i,j in beginSet:
                for dx,dy in directions:
                    new_i,new_j = i+dx,j+dy
                    if 0 <= new_i < n and 0 <= new_j < n and not grid[new_i][new_j]:
                        if (new_i,new_j) in endSet:
                            return dist-1
                        newSet.add((new_i,new_j))
            
            beginSet = newSet
        
        return -1


        

            