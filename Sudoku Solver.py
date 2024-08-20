from typing import List

def solveSudoku( board: List[List[str]]) -> None:
    numSet = set([str(i) for i in range(1,10)])
    hashmap_row = {k:numSet.copy() for k in range(9)}
    hashmap_col = {k:numSet.copy() for k in range(9)}
    hashmap_box = {k:numSet.copy() for k in range(9)}
    solve = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            box_index= (i//3)*3 + (j//3)
            if board[i][j] ==  ".": 
                solve.append([i,j,box_index])
                continue
            hashmap_row[i].remove(board[i][j])
            hashmap_col[j].remove(board[i][j])
            hashmap_box[box_index].remove(board[i][j])
    
    for i in range(len(solve)):
        row,col,box = solve[i]
        solve[i].append(hashmap_row[row].intersection(hashmap_col[col].intersection(hashmap_box[box])))
        
    def solver(carry):
        if not carry:
            return True
        row,col,box, options = carry.pop()
        for option in options:
            if option in hashmap_row[row] and option in hashmap_col[col] and option in hashmap_box[box]:
                hashmap_row[row].remove(option)
                hashmap_col[col].remove(option)
                hashmap_box[box].remove(option)
                board[row][col] = option
                if solver(carry):return True
                hashmap_row[row].add(option)
                hashmap_col[col].add(option)
                hashmap_box[box].add(option)
                board[row][col] = '.'
        carry.append([row, col, box, options])
        return False
    
    solver(solve)       
    