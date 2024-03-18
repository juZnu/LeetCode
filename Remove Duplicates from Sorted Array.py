from typing import List


def removeDuplicates( nums: List[int]) -> int:
    l,r = 0,1
    while r < len(nums) > l:
        if not nums[l] == nums[r] :
            nums[l+1],nums[r] = nums[r],nums[l+1]
            l += 1
        r +=1
    return l+1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,1,2]))