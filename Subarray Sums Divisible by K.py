def subarraysDivByK( nums, k):
    carrySumDict = {0:1}
    carrySum = 0
    res = 0
    for ele in nums:
        carrySum += ele
        carry = carrySum % k
        res += carrySumDict[carry] if carrySumDict.get(carry,0)  else 0
        carrySumDict[carry] = carrySumDict.get(carry,0) + 1
    return res
print(subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))