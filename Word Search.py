from typing import List


def exist( board: List[List[str]], word: str) -> bool:
    def nextword(row,col,next_word):
        if not next_word:
            return True
        result = False
        directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        for row,col in directions:
            if  0 <= row < len(board) and 0<= col < len(board[0]) and board[row][col] == next_word[0] and (row,col) not in visited:
                visited.add((row,col))
                result = result or nextword(row,col,next_word[1:])
            
        return result

    for row in range(len(board)):
        for col in range(len(board[0])):
            visited = set()
            visited.add((row,col))
            if board[row][col] == word[0] and nextword(row,col,word[1:]):
                return True
    return False

print(exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))