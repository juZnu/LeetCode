class Solution:
    def tribonacci(self, n: int) -> int:
        T0,T1,T2 = 0,1,1
        if not n: return T0
        for i in range(2,n):
            tmp = T0+T1+T2
            T0 = T1
            T1 = T2
            T2 = tmp
        return T2 
        