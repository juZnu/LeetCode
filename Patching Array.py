def minPatches( nums, n):
    carrySum = set([0])
    carry = 0
    patch = 0

    j = 1
    for i in nums:
        
        while j<i:
            if j-carry not in carrySum:
                patch += 1 
                carry += j-carry
                carrySum.add(j-carry)
            j+=1  
        carry +=i
        carrySum.add(carry)
        j +=1
        
    return patch    
  
                
                
print(minPatches(nums = [1,5,10], n = 20))