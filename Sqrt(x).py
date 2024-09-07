class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        l = 1
        r = x
        while l+1 < r:
            mid = l+ (r-l)//2
            sq = mid*mid
            if  sq < x:
                l = mid 
            elif sq > x:
                r = mid
            else:
                return mid

        return l 