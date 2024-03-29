class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(ele):
            return ele in 'aeiou'
        result = 0
        for ele in s[:k]:
            result += 1 if isVowel(ele) else 0
        carry = result
        for index in range(k,len(s)):
            if s[index-k] != s[index]:
                carry -= 1 if isVowel(s[index-k]) else 0
                carry += 1 if isVowel(s[index]) else 0
                result = max(result,carry)
        return result
            
        