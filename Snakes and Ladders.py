from typing import List


def snakesAndLadders( board: List[List[int]]) -> int:
    n = len(board)
    memo = {}
    visited = set()
    for i in range(n//2):
        if i%2:
            board[i],board[-i-1] = board[-i-1][::-1],board[i][::-1]
        else:
            board[i],board[-i-1] = board[-i-1],board[i]

    def climb(i,j):
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        if (i,j) in visited:
            return float('inf')

        if i ==n-1  and j == n-1:return 0
        
        visited.add((i,j))
        a,b = float('inf'),float('inf')
        if board[i][j] != -1:
            new_i = board[i][j]//n
            new_j = board[i][j]%n - 1
            a = 1+climb(new_i,new_j)

        new_i,new_j = i,j+1

        if new_j == n:
            new_i += 1
            new_j = 0

        b = 1+climb(new_i,new_j)
        memo[(i,j)] = min(a,b)

        return memo[(i,j)]
            
    return climb(0,0)
    
print(snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))