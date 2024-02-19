def wiggle_sort( nums):
    check = True
    for i in range(len(nums)-1):
        if check and nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
        elif (not check) and nums[i] < nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i] 
        check != check  
    return nums
print(wiggle_sort(nums= [3, 5, 2, 1, 6, 4]))