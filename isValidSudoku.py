def isValidSudoku(board):
    row =[{} for _ in range(9)]
    column =[{} for _ in range(9)]
    box =[{} for _ in range(9)]
    for r in range(9):
        for c in range(9):
            ele = board[r][c] 
            if ele == '.' :
                continue
            if (row[r].get(ele,0) or 
                column[c].get(ele,0) or 
                box[(3*(r//3))+(c//3)].get(ele,0)):
                return False
            row[r][ele] = 1
            column[c][ele] = 1
        box[(3*(r//3))+(c//3)][ele] = 1
    return True