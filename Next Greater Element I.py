def nextGreaterElement(nums1, nums2):
    hashmap = dict()
    for i in range(len(nums2)-1):
        hashmap[nums2[i]] = nums2[i+1:]
    for i in range(len(nums1)):
        boolean = True
        for ele in hashmap.get(nums1[i],[]):
            if nums1[i] < ele:
                nums1[i] = ele
                boolean =  not boolean
                break
        nums1[i] = -1 if boolean else nums1[i]
    return nums1
        
print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))