from typing import List


def removeElement( nums: List[int], val: int) -> int:
    i = 0
    j = len(nums)

    while i < j and nums[j-1] == val:
        j -= 1

    while i < j:
        if nums[i] == val:
            nums[i],nums[j-1] = nums[j-1],nums[i]
            j -= 1
        i += 1
    return i
print(removeElement(nums = [2,2,3], val = 2))