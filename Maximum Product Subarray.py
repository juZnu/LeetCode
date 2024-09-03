def maxProduct( nums) -> int:
    dp =[1 for _ in range(len(nums)+1)]

    for j in range(len(nums)):
        for i in range(j+1):
            dp[i] = max(nums[i]*dp[i-1],dp[i])

    return dp[-1]
print(maxProduct(nums = [2,3,-2,4]))