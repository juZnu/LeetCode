from typing import List
import collections

def countTriplets( arr: List[int]) -> int:
    
    carrySum = 0
    hashmap = collections.defaultdict(list)
    res = 0
    for i,ele in enumerate(arr):
        if ele in hashmap:
            pass
        carrySum ^= ele
        hashmap[carrySum].append(i)
    
    print(hashmap)

    return res

print(countTriplets(arr = [2,3,1,6,7]))