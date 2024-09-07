from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_set,col_set = set(),set()
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row_set.add(i)
                    col_set.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
