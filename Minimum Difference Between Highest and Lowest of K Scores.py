import heapq
from typing import List


def minimumDifference( nums: List[int], k: int) -> int:
    nums.sort()
    result = float('inf')
    i = 0
    while i+k-1 < len(nums):
        result = min(result,nums[i+k-1] -nums[i])  
        i += 1
    return result

print(minimumDifference(nums = [9,4,1,7],k = 2))