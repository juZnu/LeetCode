from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for a,b in operations:
            index = hashmap[a]
            nums[index] = b
            hashmap.pop(a)
            hashmap[b] = index

        return nums
            
