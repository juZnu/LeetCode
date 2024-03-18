from typing import List


def checkPossibility( nums: List[int]) -> bool:
    count = 0

    for ind in range(1,len(nums)):
        if nums[ind-1] > nums[ind]:
            nums[ind-1] = prev
            count += 1
        if count > 1:
            return False
        prev = nums[ind-1]
    return count <= 1

print(checkPossibility(nums = [3,4,2,3]))