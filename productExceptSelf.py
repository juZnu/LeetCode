def productExceptSelf(nums):
    start = 1
    length = len(nums)
    result = [1] * length
    for i in range(1,length):
        result[i] = result[i-1] * nums[i-1] if i != 0 else 1
    for i in range(-2,-1* (length+1),-1):
        start = start * nums[i+1]
        result[i] *= start            
    return result