from typing import List

def subsetsWithDup( nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    def helper(carry,index):
        result.append(carry.copy())
        if len(nums) == index:
            return
        for ind in range(index,len(nums)):
            carry.append(nums[ind])
            helper(carry,ind+1)
            carry.pop()
    helper([],0)
    return result


print(subsetsWithDup(nums = [1,2,2]))