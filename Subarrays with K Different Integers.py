from typing import List


def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    l = 0
    m = 0
    hashmapr = {}
    hashmap = {}
    result  = 0
    for r in range(len(nums)):
        hashmap[nums[r]] = hashmap.get(nums[r],0) + 1
        hashmapr[nums[r]] = hashmapr.get(nums[r],0) + 1
        while len(hashmap) > k:
            hashmap[nums[l]] -= 1
            if not hashmap[nums[l]] : 
                del hashmap[nums[l]]
                del hashmapr[nums[l]]
            l += 1
            m = l
            
        if len(hashmap) == k:
            while len(hashmapr) == k:
                hashmapr[nums[m]] -= 1
                if not hashmapr[nums[m]] :
                    hashmapr[nums[m]] += 1
                    break
                else:
                    m += 1
            result += m - l + 1
    return result

print(subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))