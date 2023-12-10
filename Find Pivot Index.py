def pivotIndex(nums):
    forward = [0]*len(nums)
    backward = [0]*len(nums)
    for i in range(len(nums)-2,-1,-1):
        backward[i] = backward[i+1] + nums[i+1]
    for i in range(1,len(nums)):
        forward[i] = forward[i-1] +nums[i-1]
        if forward[i-1] == backward[i-1]:
            return i
    return -1 if forward[-1] != backward[-1] else len(nums)-1