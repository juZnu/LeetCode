from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXORb = 0
        for ele in nums:
            aXORb ^= ele
        
        least = aXORb & -aXORb
        carry = 0
        for ele in nums:
            if not (ele & least):
                carry ^= ele
        return [carry,aXORb^carry]

        