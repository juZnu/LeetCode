from typing import List

def permute( nums: List[int]) -> List[List[int]]:
        result = []
        def permutaions(carry,num):
            if not num: 
                result.append(carry) 
                return
            for i in range(len(num)):
                permutaions(carry+[num[i]],num[:i]+num[i+1:])
        permutaions([],nums)
        return result
    
print(permute(nums=[1,2,3]))