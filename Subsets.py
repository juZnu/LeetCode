from typing import List


def subsets( nums: List[int]) -> List[List[int]]:
    result = []
    def sub(subset,i,nums):
        result.append(subset)
        for index in range(i+1,len(nums)):
            sub(subset+[nums[index]],index,nums)
    sub([],-1,nums)     
    return result
        
print(subsets(nums = [1,2,3]))
        
    