def findMin( nums):
    l = 0
    r = len(nums)-1
    while l < r-1 and nums[l] >= nums[r]:
        middle = (r+l) //2
        if nums[middle] >= nums[l]:
            l = middle
        elif nums[middle] <=nums[r]:
            r = middle
    return min(nums[l],nums[r])
print(findMin(nums = [10,1,10,10,10]))