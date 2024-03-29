from typing import List


def maxSubarrayLength( nums: List[int], k: int) -> int:
        result  = 0
        l = 0
        hashMap = {}
        for r in range(len(nums)):
                hashMap[nums[r]] = hashMap.get(nums[r],0) + 1
                while hashMap[nums[r]] > k:
                        hashMap[nums[l]] -= 1
                        l+=1
                result = max(result,r+1-l)
        return result
                
print(maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))