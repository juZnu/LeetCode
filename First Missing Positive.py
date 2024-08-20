from typing import List
def firstMissingPositive( nums: List[int]) -> int:
        
    for i in range(len(nums)):
        while nums[i] != i+1 and 0 < nums[i] <= len(nums):
            tmp1 = nums[i]
            tmp2 = nums[nums[i]-1]
            nums[i] = tmp2
            nums[tmp1-1] = tmp1

    for i in range(len(nums)):
        if i+1 != nums[i]: return i+1
        
    return len(nums)

print(firstMissingPositive([3,4,-1,1]))