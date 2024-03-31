from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = {}
        result = 0
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        for k,v in hashmap.items():
            if v == 1: return -1
            result += v//3 + (0 if not v % 3 else 1)
        return result