from typing import List


def subsetsWithDup( nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    def backtrack(array,i):
        if i > len(nums):
            return
        if i == len(nums):
            result.append(array.copy())
            return



        array.append(nums[i])
        backtrack(array,i+1)
        ele = array.pop()

        while  i < len(nums)-1 and ele == nums[i+1]:
            i += 1

        backtrack(array,i+1)

    backtrack([],0)
    return result

print(subsetsWithDup(nums = [1,2,2]))