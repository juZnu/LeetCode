from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashMap = {}
        for ele in nums:
            hashMap[ele] = hashMap.get(ele,0) + 1
        count  = 0
        maxele = 0
        for k,v in hashMap.items():
            if v> maxele:
                count = 0
                maxele = v
            count += v if v == maxele  else 0
        return count

        