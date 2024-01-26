def search( nums, target):
    i = 0
    j = len(nums)-1
    while i<=j:
        middle = (i+j)//2
        if nums[middle] >target:
            j = middle -1
        elif nums[middle] < target:
            i = middle +1
        else:
            return middle
    return -1
            
    
print(search(nums = [-1,0,3,5,9,12], target = 2))