class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        row_start,col_start= 0,0
        keys,visited  = 0,set()
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        res = float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if ord('a') <= ord(grid[i][j]) <= ord('z'):
                    mask = ord(grid[i][j])-ord('a')
                    keys |= (1<<(mask))

                elif grid[i][j] == '@':
                    row_start = i
                    col_start = j
        
        queue = collections.deque()
        queue.append((row_start,col_start,0,0))

        while queue:

            row,col,collected,steps = queue.popleft()

            if (row,col,collected) in visited:
                continue
            
            visited.add((row,col,collected))

            if collected == keys:
                res = min(res,steps)
                continue
            
            for dx,dy in directions:
                new_row,new_col = row+dx,col+dy

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    new_collected = collected
                    
                    if grid[new_row][new_col] == '#':
                        continue
                    
                    elif 'a' <= grid[new_row][new_col] <= 'z':
                        key = ord(grid[new_row][new_col]) - ord('a')
                        new_collected |= (1 << key)

                    elif 'A' <= grid[new_row][new_col] <= 'Z':
                        key = ord(grid[new_row][new_col]) - ord('A')
                        if not (new_collected & (1 << key)):
                            continue
                    
                    queue.append((new_row,new_col,new_collected,steps+1))
        
        return res if res != float('inf') else -1
