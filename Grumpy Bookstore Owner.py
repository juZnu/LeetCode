from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        res = 0
        carry = 0

        for i in range(len(customers)):
            if not grumpy[i]:
                res += customers[i]

        for i in range(minutes):
            carry+= customers[i] if grumpy[i] else 0

        grumpy_count = carry 

        for i in range(minutes,len(customers)):
            carry += customers[i] if grumpy[i] else 0
            carry -= customers[i-minutes] if grumpy[i-minutes] else 0
            grumpy_count = max(grumpy_count,carry)

        return res+grumpy_count