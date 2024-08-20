from typing import List


def minSwaps( nums: List[int]) -> int:
    count1 = sum(nums)
    carry1 = sum(nums[-count1:])
    res = count1-carry1
    for i in range(len(nums)):
        if nums[i-count1]:
            carry1 -= 1
        
        carry1 += nums[i]
        res = min(res,count1-carry1)
    
    return res

print(minSwaps(nums = [1,1,0,0,1]))