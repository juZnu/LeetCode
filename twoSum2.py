def twoSum( numbers, target):
    i = 0
    j = len(numbers) - 1
    while i<j:
        s= numbers[i] +numbers[j] 
        if s > target:
            j -= 1
        elif s <target:
            i += 1
        else:
            return [i+1,j+1]