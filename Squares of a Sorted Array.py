from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1
    result = [0 for _ in nums]
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            result[r-l] = nums[l] * nums[l]
            l += 1
        else:
            result[r-l] = nums[r] * nums[r]
            r -= 1
    return result

print(sortedSquares(nums = [-4,-1,0,3,10]))