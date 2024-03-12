from typing import List


def combinationSum2( candidates: List[int], target: int) -> List[List[int]]:
    result = []
    def combinations(array,candidate,target):
        prev = float('inf')
        if not target:
            result.append(array)
            return
        elif target < 0:
            return
        for i in range(len(candidate)):
            if prev != candidate[i]:
                combinations(array+[candidate[i]],candidate[i+1:], target- candidate[i])
            prev = candidate[i]
    combinations([],sorted(candidates),target)
    return result

print(combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))