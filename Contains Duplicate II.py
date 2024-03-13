from typing import List


def containsNearbyDuplicate( nums: List[int], k: int) -> bool:
    hashmap = {}
    for index,key in enumerate(nums):
        if hashmap.get(key,0) and index + 1 - hashmap[key] <= k:
            return True
        hashmap[key] = index+1
    return False
    
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))