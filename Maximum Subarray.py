class Solution:
    def maxSubArray(self, nums) -> int:
        carrySum = 0
        result = float('-inf')
        minValue = 0
        
        for v in nums:
            carrySum += v
            result = max(result, carrySum - minValue)
            minValue = min(minValue,carrySum)
            
        return result