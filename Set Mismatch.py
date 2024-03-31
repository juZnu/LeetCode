from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashset =set()
        result = []
        for i in nums:
            if i in hashset:
                result.append(i)
            else:
                hashset.add(i)
        for i in range(1,len(nums)+1):
            if i not in hashset:
                result.append(i)
                return result

        