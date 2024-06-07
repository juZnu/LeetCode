class Solution:
    def totalNQueens(self, n: int) -> int:

        def checkQueens(row,index,carrySet):
            for k,v in carrySet.items():
                if index in [v,v-(row-k), v+(row-k)]:
                    return False   
            return True        
        
        def helper(i,carry):
            if i==n:
                res[0] += 1
                return
            for j in range(n):
                if checkQueens(i,j,carry):
                    carry[i] = j
                    helper(i+1,carry)
                    carry.pop(i)

        res = [0]    
        helper(0,{})
        return res[0]
