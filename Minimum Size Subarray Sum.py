def minSubArrayLen( target, nums):
    l = 0
    carrySum = 0
    result = float('inf')
    for r in range(len(nums)):
        carrySum += nums[r]
        while carrySum >= target  and l <= r:
                result = min(result, r - l + 1)
                carrySum -= nums[l]
                l += 1
    return 0 if result == float('inf') else result
              
                
print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))