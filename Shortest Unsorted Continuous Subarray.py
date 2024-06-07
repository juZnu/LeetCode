from typing import List


def findUnsortedSubarray( nums: List[int]) -> int:
    l = 0
    r = len(nums)-1
    while l < len(nums)-1 and nums[l] <= nums[l+1]:
        l += 1
    
    while r > 0 and nums[r] >= nums[r-1]:
        r -= 1
    
    if l == len(nums)-1 : return 0

    minVale  = min(nums[l:r+1])
    maxValue = max(nums[l:r+1])

    while l >=0 and minVale < nums[l]:
        l -= 1
    l += 1

    while r < len(nums) and maxValue > nums[r]:
        r += 1  
    r -= 1
    return  r-l+1

print(findUnsortedSubarray([2,1]))