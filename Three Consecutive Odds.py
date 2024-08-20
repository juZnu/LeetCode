class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l = 0
        for r in range(len(arr)):
            l = r
            if arr[r]%2: break

        for r in range(l,len(arr)):
            if not arr[r]%2:
                l = r+1
            if (r-l+1) == 3:
                return True
            
        return False
        