from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    def search(word,row,col,visited):
        if not word: return True
        neighbours = [(row+1,col),(row-1,col),(row,col-1),(row,col+1)]
        result = False
        for i,j in neighbours:
            if 0<= i< len(board) and 0<= j < len(board[0]) and (i,j) not in visited and board[i][j] == word[0]:
                visited.add((i,j))
                result = result or search(word[1:],i,j,visited)
                visited.remove((i,j))
        return result
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0]:
                if search(word[1:],row,col,{(row,col)}):return True
    return False
                 
            
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))