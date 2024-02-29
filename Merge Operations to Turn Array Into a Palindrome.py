def minimumOperations(nums):
    l,r = 0,len(nums)-1
    forwardSum,backwadSum = nums[l],nums[r]
    count = 0
    while l < r:
        if forwardSum < backwadSum:
            l += 1
            forwardSum += nums[l]
            count += 1
        elif backwadSum < forwardSum:
            r -=1
            backwadSum +=nums[r]
            count += 1
        else:
            l +=1
            r -=1
            forwardSum = nums[l]
            backwadSum = nums[r]
    return count    
    
print(minimumOperations(nums =[1,2,3,4]))