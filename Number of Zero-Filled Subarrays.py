from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        l = 0
        r = 0
        while r < len(nums):
            while r < len(nums) and not nums[r]:
                result += r-l+1
                r += 1
            r += 1
            l=r
        return result
