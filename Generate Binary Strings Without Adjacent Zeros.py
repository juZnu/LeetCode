class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backTracking(binStr):
            if len(binStr) == n:
                res.append(binStr)
                return
            if not(binStr and binStr[-1] =='0'):
                backTracking(binStr+'0')
            backTracking(binStr+'1')

        backTracking('')
        return res
        