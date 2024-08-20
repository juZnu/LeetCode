def relativeSortArray( arr1, arr2):
    hashmap = {}
    for ele in arr1:
        hashmap[ele] = hashmap.get(ele,0) + 1
    
    res = []
    carry = []

    for ele in arr2:
        if ele in hashmap:
            carry.extend([ele]*hashmap[ele])
            hashmap.pop(ele)
    
    for k,v in hashmap.items():
        carry.extend([k]*v)

    carry.sort()

    return res + carry
    
print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
