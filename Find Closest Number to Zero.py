from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = float('inf')
        for ele in nums:
            if abs(ele) < abs(result):
                result = ele
            if abs(ele) == abs(result):
                result = max(ele,result)
        return result 
        