class Solution(object):
    def minFallingPathSum(self, matrix):
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[i])):
                matrix[i][j] += min(matrix[i+1][j-1] if j-1>=0 else float('inf'),matrix[i+1][j],matrix[i+1][j+1] if j+1 < len(matrix[i]) else float('inf'))

        return min(matrix[0])