from typing import List


def search( nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] < nums[r]:
            r = mid 
        else:
            l = mid + 1
        
        
    start = l
    
    def BinarySearch(l,r,target):
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return l if nums[l] == target else -1
        
        
    if target > nums[-1]:
        return BinarySearch(0,l-1,target)
    return BinarySearch(l,len(nums)-1,target)

print(search(nums = [4,5,6,7,0,1,2], target = 0))

