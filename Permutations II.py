from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    result = []
    def helper(carry,array):
        if not array:
            result.append(carry.copy())
            return
        for i in range(len(array)):
            carry.append(array[i])
            helper(carry,array[:i]+array[i+1:])
            carry.pop()
    helper([],nums)
    return result

print(permuteUnique([1,1,2]))