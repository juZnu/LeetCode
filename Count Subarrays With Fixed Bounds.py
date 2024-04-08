from typing import List

def countSubarrays( nums: List[int], minK: int, maxK: int) -> int:
    l = 0
    minfound , maxfound = False,False
    minindex , maxindex = 0,0
    result = 0
    for r in range(len(nums)):
        if nums[r] == minK:
            minfound = True
            minindex = r
        if nums[r] == maxK:
            maxfound = True
            maxindex = r
        if nums[r] > maxK or nums[r] < minK:
            minfound , maxfound = False,False
            l = r+1
        elif maxfound and minfound:
            result += min(maxindex,minindex) - l+ 1
    return result
            
            
            

print(countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
print(countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))