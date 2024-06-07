from typing import List



def search( nums: List[int], target: int) -> int:
    def BinarySearch(l,r,target):
        while l < r:
            mid = l+((r-l)//2)
            
            if nums[mid] < target:
                l= mid + 1
            elif nums[mid] > target:
                r= mid - 1
            else:
                return mid
        return l if nums[l] == target else -1
    
    l = 0
    r = len(nums)-1
    while l<r-1:
        mid = l + ((r-l)//2)
        if nums[mid] > nums[l]:
            l = mid
        else:
            r = mid
            
    l = l if nums[l] < nums[r] else r
    
    if nums[-1] >= target:
        return  BinarySearch(l,len(nums)-1,target)
    else:
        return BinarySearch(0,l,target)
        
        


print(search(nums = [1,3,5], target = 1))