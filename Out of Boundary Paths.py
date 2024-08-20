import collections


def findPaths( m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    queue = collections.deque()
    queue.append([startRow,startColumn,0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    res = 0

    while queue:
        row,col,length = queue.popleft()

        if length >= maxMove: continue

        for dr,dc in directions:
            if (0 <= row+dr < m ) and (0 <= col+dc  < n):
                queue.append([row+dr,col+dr,length+1])
            else:
                res += 1
    
    return res

print(findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
                

