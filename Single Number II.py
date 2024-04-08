from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for ele in nums:
            if ele not in hashmap:
                hashmap[ele] = 0
            hashmap[ele] += 1
        for k,v in hashmap.items():
            if v== 1:
                return k