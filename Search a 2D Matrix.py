def binarySearch(nums,target):
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
def searchMatrix( matrix, target):
    i = 0
    j = len(matrix)-1
    while  i<j:
        middle  = (j+i)//2
        if matrix[middle][0] > target:
            j = middle-1
        elif matrix[middle][0] < target:
            if matrix[middle][-1] > target:
                i= middle 
                j = middle 
            elif matrix[middle][-1] < target:
                i = middle +1
            else:
                return True
        else:
            return True
    return not binarySearch(matrix[i],target) == -1 if i ==j else False
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 20))
print(searchMatrix(matrix = [[1],[3]], target = 0))