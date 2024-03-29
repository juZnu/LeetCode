from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    total = lambda n: n * (n+1) // 2 
    l = 0
    middle = 0
    r = 0
    result = 0
    product = 1
    while  r<len(nums) and k:
        if product >= k:
            a= total(r-1-l) 
            b = total(middle) 
            result += a - b
            middle = r
            while product >= k and l < r:
                product /= nums[l]
                l += 1
                middle -= 1
        else:
            product *= nums[r]
            r += 1
    return result + total(r-l) - total(middle)
            
    

print(numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
print(numSubarrayProductLessThanK(nums = [1,1,1], k = 2))
print(numSubarrayProductLessThanK(nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3], k = 19))