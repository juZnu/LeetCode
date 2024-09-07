from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = res = nums[0]

        for val in nums[1:]:
            if val < 0:
                maxProd,minProd = minProd,maxProd
            
            maxProd = max(val,maxProd*val)
            minProd = min(val,minProd*val)
            res = max(res,maxProd)

        return res
