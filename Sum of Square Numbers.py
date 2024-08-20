import math


def judgeSquareSum(c):
    end = int(math.sqrt(c)+1)
    l = 0
    r = end
    while l < r:
        mid = l + ((r-l)//2) 
        carry = c - (mid*mid)
        second = math.sqrt(carry)
        div,mod = divmod(second,1)
        if not carry: return True
        if not div:
            l = mid+1
        elif mod:
            r = mid
        else:
            return True
    return False
    

print(judgeSquareSum(8))
        