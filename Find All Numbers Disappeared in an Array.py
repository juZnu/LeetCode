def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i+1)
    return missing