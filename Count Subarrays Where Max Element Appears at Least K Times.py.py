from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        value = max(nums)
        result = 0
        count = 0
        prev = 0
        for i in range(len(nums)):
            if value == nums[i]: count +=1
            if count == k:
                j = prev
                while nums[j] != nums[i]:
                    j += 1
                result += (j+1- prev) * (len(nums) - i)
                prev = j+1
                count -=1
        return result

