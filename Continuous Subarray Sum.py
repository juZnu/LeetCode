def checkSubarraySum( nums, k):
    prefix = {0:-1}
    carrySum = 0
    zeroindex = -2
    for index,value in enumerate(nums):
        carrySum += value
        remainder = carrySum % k 
        if remainder not in prefix:
            prefix[remainder] = index
        elif index - prefix[remainder] > 1:
            return True
        if not value:
            if zeroindex == -2:
                zeroindex = index
            elif index - zeroindex  == 1:
                return True
    return False
    
print(checkSubarraySum(nums = [5,0,0,0], k = 3))