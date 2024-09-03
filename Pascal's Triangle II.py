class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        while rowIndex:
            for index in range(len(res)-1,0,-1):
                res[index] += res[index-1]
            res.append(1)
            rowIndex -= 1
        return res