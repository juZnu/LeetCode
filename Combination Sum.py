from typing import List

def combinationSum( candidates: List[int], target: int) -> List[List[int]]:
    result = []
    def combinations(candidate,array,target):
        if target ==0:
            result.append(candidate)
            return
        elif not array or target <0:
            return
        combinations(candidate+[array[0]],array,target-array[0])
        combinations(candidate,array[1:],target)
    combinations([],candidates,target)
    return result
    
print(combinationSum(candidates = [2,3,6,7], target = 7))