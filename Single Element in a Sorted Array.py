from typing import List


def singleNonDuplicate( nums: List[int]) -> int:
    l = 0
    r = len(nums)-1
    while r-l > 2:
        mid = l+((r-l)//2)
        if nums[mid] == nums[mid-1]:
            l = mid +1
        else:
            r = mid
    return  nums[r] if nums[l] == nums[l+1] else nums[l]

print(singleNonDuplicate(nums = [3,3,7,7,10,11,11]))

print(singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))