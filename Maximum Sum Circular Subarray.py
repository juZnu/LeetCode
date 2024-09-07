from typing import List


def maxSubarraySumCircular( nums: List[int]) -> int:
    carrySum = 0
    maxSum = nums[0]
    index = 0
    n = len(nums)
    for val in nums:
        if index == n:
            carrySum = val
            index = 0
        else:    
            carrySum = max(val,carrySum+val)
        maxSum = max(carrySum,maxSum)
        index += 1
    
    for val in nums:
        if index == n:
            carrySum = val
            index = 0
        else:    
            carrySum = max(val,carrySum+val)
        maxSum = max(carrySum,maxSum)
        index += 1
    
    return maxSum
print(maxSubarraySumCircular([5,-3,5]))