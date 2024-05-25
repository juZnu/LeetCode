from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += nums[i] - i
        return len(nums) - res 

        