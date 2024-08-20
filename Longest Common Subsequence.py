def longestCommonSubsequence( text1: str, text2: str) -> int:
    dp = [0 for _ in range(len(text1)+1)]
    carry = dp.copy()
    
    for ele in text2:
        for i in range(1,len(dp)):
            if text1[i-1] == ele:
                carry[i] = 1 + dp[i-1]
            else:
                carry[i] = max(dp[i],carry[i-1])
        dp = carry.copy()

    return dp[-1]

print(longestCommonSubsequence(text1 = "abcba", text2 = "abcbcba" ))