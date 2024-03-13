from typing import List

def searchInsert( nums: List[int], target: int) -> int:
        l = 0
        r  = len(nums)
        while l < r:
            middle = l+(r-l)//2
            if nums[middle]< target:
                l = middle+1
            elif nums[middle] > target:
                r = middle
            elif nums[middle] == target:
                return middle
        return r
            
print(searchInsert(nums = [1,3,5,6], target = 0))