from typing import List


def solveNQueens( n: int) -> List[List[str]]:
    result = []
    def checkQueens(row,index,carrySet):
        for k,v in carrySet.items():
            if index in [v,v-(row-k), v+(row-k)]:
                return False   
        return True        
    
    def helper(i,carry,board):
        if i==n:
            result.append(board)
            return
        row = ['.' for _ in range(n)]
        for j in range(n):
            if checkQueens(i,j,carry):
                row[j] = 'Q'
                carry[i] = j
                board.append(''.join(row))
                helper(i+1,carry,board.copy())
                board.pop()
                carry.pop(i)
                row[j] = '.'
            
    helper(0,{},[])
    return result
print(solveNQueens(4))