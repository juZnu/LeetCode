def subarraySum( nums, k):
    carryDict = {0:1}
    result = 0
    carry_sum = 0
    for ele in nums:
        carry_sum += ele
        sum_ = carry_sum - k
        result += carryDict.get(sum_,0)
        carryDict[carry_sum] = carryDict.get(carry_sum,0) + 1
    return  result
            
print(subarraySum(nums = [1,1,1], k = 2))
print(subarraySum(nums = [1], k = 0))