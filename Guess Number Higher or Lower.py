# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        while l < n:
            middle = l + (n-l)//2
            number = guess(middle)
            if not number:
                return middle
            elif number > 0:
                l = middle+1
            elif number < 0:
                n = middle
        return l
        
        
        