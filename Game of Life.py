def gameOfLife(board):
    def neighbours_count(board,i_index,j_index):
        sum = 0
        for i in range(max(0,i_index-1),min(len(board),i_index+2)):
            for j in range(max(j_index-1,0), min(len(board[i]),j_index+2)):
                if board[i][j] == 1 or board[i][j] == 2:
                    sum += 1
        return sum 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] :
                if 2 > neighbours_count(board,i,j) or  neighbours_count(board,i,j)> 3:
                    board[i][j] = 2
            else:
                if  neighbours_count(board,i,j) == 3:
                    board[i][j] = 3
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] ==3:
                board[i][j] = 1
            elif board[i][j] == 2:
                board[i][j] = 0
    return board
print(gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

