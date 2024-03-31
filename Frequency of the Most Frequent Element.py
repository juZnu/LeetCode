from collections import deque
from typing import List


def maxFrequency( nums: List[int], k: int) -> int:
    nums.sort()
    carrySum = k
    result = 0
    l = 0
    for r in range(len(nums)):
        carrySum += nums[r]
        if carrySum // nums[r] >= r-l+1:
            result = max(result,r-l+1)
        while carrySum // nums[r] < r-l+1 :
            carrySum -= nums[l]
            l += 1
    return result
            
            

print(maxFrequency(nums = [1,2,4,4,1,3,3], k = 5))