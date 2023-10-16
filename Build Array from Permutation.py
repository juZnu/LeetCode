def buildArray( nums):
    result =[0]* len(nums)
    for i in nums:
        result[i] = nums[nums[i]]
    return result