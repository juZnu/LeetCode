def findMin( nums):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = l + (r-l) // 2
        if nums[mid] < nums[l]:
            r = mid
        else:
            l = mid+1
    return nums[l]

print(findMin([4,5,6,7,0,1,2]))
