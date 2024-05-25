import collections
def wallsAndGates(rooms):
    gates = []
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            
            if rooms[i][j] == 0:
                gates.append([i,j])
    
    directions = [(-1,0),(1,0),(0,1),(0,-1)]

    for row,col in gates:
        queue = collections.deque()
        queue.append([row,col,0])
        visited = set()
        visited.add((row,col))
        while queue:
            r,c,length = queue.popleft()
            
            if length > rooms[r][c] > 0:
                continue
            
            for dr,dc in directions:
                rdr = r+dr
                cdc = c+dc
                
                if 0<= rdr < len(rooms) and 0<= cdc < len(rooms[rdr]) and (rdr,cdc) not in visited:
                    if 1+length < rooms[rdr][cdc] and rooms[rdr][cdc] > 0:
                        rooms[rdr][cdc] = 1+length
                        queue.append([rdr,cdc,1+length])    
                        visited.add((rdr,cdc))            
    print(rooms)           

print(wallsAndGates(rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))