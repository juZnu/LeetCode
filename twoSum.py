def twoSum(nums, target):
    index = dict()
    for i in range(len(nums)):
        if index.get(target-nums[i],0):
            return [index[target-nums[i]]-1,i]
        index[nums[i]] = i+1
    return 0