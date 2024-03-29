def findLength(nums1, nums2):
    len1 , len2 = len(nums1),len(nums2)
    dp = [[0 for _ in range(len1)] for _ in range(len2)]
    carry = 0
    result = 0
    for i in range(len1-1,-1,-1):
        for j in range(len2-1,-1,-1):
            if nums1[i] == nums2[j]:
                carry = 1 +( dp[j+1][i+1] if  i+1 < len1 and  j+1 < len2 else 0)    
                result = max(result,carry)    
            else:
                carry = 0
            dp[j][i] = carry
    return result 
            
print(findLength(nums1 = [1,2,3,2,1], nums2 =[3,2,1,4]))