def findMin( nums):
    i = 0
    j = len(nums)-1
    if nums[i] < nums[j]:
        return nums[i]
    while i+1 < j:
        middle = (i+j)//2
        if nums[middle] > nums[i]:
            i = middle
        elif nums[middle] < nums[j]:
            j = middle
    return nums[j]
