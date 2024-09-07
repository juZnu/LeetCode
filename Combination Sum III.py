class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backTracking(i,carrySum,carryRes):
            if carrySum == n:
                if len(carryRes) == k:res.append(carryRes.copy())
                return 
            if carrySum > n or i >9: return 
            
            for nextI in range(i+1,10):
                if carrySum+nextI > n: break
                carryRes.append(nextI)
                backTracking(nextI,carrySum+nextI,carryRes)
                carryRes.pop()
            
            return 
        backTracking(0,0,[])
        return res
            