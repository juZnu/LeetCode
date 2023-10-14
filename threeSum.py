def twoSum(nums,target):
    start = 0
    end = len(nums) - 1
    result = []
    while start < end:
        if nums[start]+nums[end] > target :
            end -= 1
        elif nums[start]+nums[end] < target :
            start += 1 
        else:
            while nums[start+1] == nums[start] and start < end-1:
                start += 1
            while nums[end-1] == nums[end] and start+1 < end:
                end -= 1   
            result.append([nums[start],nums[end]])
            start += 1
            end -= 1
        return result

def threeSum(nums):
    nums.sort()
    res = list()
    for i,value in enumerate(nums[:-1]):
        if value == nums[i-1] and i != 0:
            continue
        restwo = twoSum(nums[i+1:],(-1) *value)
        if restwo:
            for ele in restwo:
                res += [[value,ele[0],ele[1]]]
    return res