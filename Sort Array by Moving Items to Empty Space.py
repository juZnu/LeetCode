from typing import List

def sortArray( nums: List[int]) -> int:
    front = 0
    back = 0
    for i,ele in enumerate(nums):
        if not ele: 
            continue
        if i == ele:
            back += 1  
        elif i == ele-1:
            front += 1
        else:
            back += 1
            front += 1
            
    return min(front, back) 

print(sortArray(nums = [3,2,1,6,7,4,5,0]))  