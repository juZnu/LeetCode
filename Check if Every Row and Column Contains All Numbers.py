class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        length = len(matrix)
        num_set = set(list(range(1,length+1)))
        rows = [num_set.copy() for _ in range(length)]
        columns = [num_set.copy() for _ in range(length)]

        for i in range(length):
            for j in range(length):
                ele = matrix[i][j]
                if ele in rows[i]: rows[i].remove(ele)
                if ele in columns[j]: columns[j].remove(ele)

        for ele in rows:
            if ele: return False

        for ele in columns:
            if ele: return False

        return True
        