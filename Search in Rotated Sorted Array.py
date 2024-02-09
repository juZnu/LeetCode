def Binarysearch( nums, target):
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
def search(nums, target):
    i = 0
    j = len(nums)-1
    while i<j-1 and nums[i] > nums[j]:
        middle =(i+j)//2
        if nums[middle] > nums[i]:
            i = middle
        elif nums[middle] < nums[j]:
            j = middle
        else:
            break
    starting = i if nums[i] < nums[j] else j
    i = 0 if target > nums[-1] else starting
    j = len(nums)-1 if target <= nums[-1] else starting-1
    result = Binarysearch(nums[i:j+1],target)
    return -1 if result == -1 else i+ result
print(search(nums = [3,5,1], target = 1))