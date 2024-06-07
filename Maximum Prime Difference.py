from math import isqrt
from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def checkPrime(n):
            if n==1: return False
            for i in range(2,isqrt(n)+1):
                if not n%i : return False
            return True

        first = 0
        while not checkPrime(nums[first]):
            first += 1
        
        last = len(nums)-1
        while not checkPrime(nums[last]):
            last -= 1
            
        return last - first

            