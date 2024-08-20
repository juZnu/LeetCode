from typing import List


def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    res = 0
    carrySum = sum(nums[:2])
    i = 2
    while i < len(nums):
        if carrySum < nums[i]:
            res = max(res,carrySum)
            if i+2 < len(nums):carrySum = nums[i] +nums[i+1]
            else: carrySum = 0
            i += 1
        else:
            carrySum += nums[i]
        i += 1

    return res

print(largestPerimeter(nums = [1,12,1,2,5,50,3]))