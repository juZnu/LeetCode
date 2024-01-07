def sortArray(nums):
    result = []
    i = 0
    j = 0
    if len(nums) >2:
        front = sortArray(nums[:(len(nums)//2)])  
        back = sortArray(nums[(len(nums)//2):]) 
    else:
        front = nums[:1]
        back = nums[1:]
    while i <len(front) and j < len(back):
        if front[i] <back[j]:
            result.append(front[i])
            i += 1
        else:
            result.append(back[j])
            j += 1
    if i< len(front):
        result.extend(front[i:])
    elif j < len(back):
        result.extend(back[j:])
    return result
  
print(sortArray(nums = [9,8,7,9,7,12,8,8,9,5]))