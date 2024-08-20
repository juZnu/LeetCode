class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquare(n):
            res = 0
            while n:
                res += (n%10)**2
                n //= 10
            return res
        sp = sumOfSquare(n)
        fp = sumOfSquare(sumOfSquare(n))
        while sp != fp and fp!= 1:
            sp = sumOfSquare(sp)
            fp = sumOfSquare(sumOfSquare(fp))

        return  fp == 1 
            
        