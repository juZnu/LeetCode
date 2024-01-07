def sortColors( nums):
    one,zero,two =0,0,0
    for ele in nums:
        if ele == 0:
            zero += 1
        elif ele == 1:
            one += 1
        else:
            two += 1
    i = 0
    while zero > 0:
        nums[i] = 0
        i += 1
        zero -=1
    while one > 0:
        nums[i] = 1
        i += 1
        one -=1
    while two > 0:
        nums[i] = 2
        i += 1
        two -=1
    return nums
        
    
print(sortColors(nums = [2,0,2,1,1,0]))