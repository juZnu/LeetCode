from collections import deque
from typing import List


def countSubarrays( nums: List[int], k: int) -> int:
    stack = []
    value = max(nums)
    result = 0
    for i in range(len(nums)):
        if value == nums[i]: stack.append(i)
    prev = 0
    for i in range(len(stack)-k+1):
        result += (stack[i]+1 - prev) * ( len(nums) - stack[i+k-1])
        prev = stack[i]+1
    return result
            
    
print(countSubarrays(nums = [1,3,2,3,3], k = 2))