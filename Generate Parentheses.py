class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def BackTracking(openB,closeB,strP):
            if not openB and not closeB:
                res.append(strP)
                return
            if openB: BackTracking(openB - 1, closeB,strP+'(')
            if closeB > openB: BackTracking(openB, closeB - 1,strP+')')

        BackTracking(n,n,'')
        return res