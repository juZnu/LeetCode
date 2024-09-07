class Solution:
    def wordBreak(self,s, words):
        words = set(words)
        dp = [False for _ in s]
        true_index = [0]  
        for i in range(len(s)):
            for index in true_index[::-1]:
                if s[index:i+1] in words:
                    dp[i] = True
                    true_index.append(i+1)
                    break
                
        return dp[-1]
            