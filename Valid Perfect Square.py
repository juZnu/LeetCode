class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1 : return True
        l = 0
        r = num
        while l+1 < r:
            middle = (l+r)//2
            if middle * middle < num:
                l = middle
            elif middle * middle > num:
                r = middle
            else:
                return True
        return False

