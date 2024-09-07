class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1]) + 1
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res,matrix[i][j])

        return res * res
                
        
        
