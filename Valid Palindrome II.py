class Solution(object):
    def validPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j :
            if s[i] != s[j]:
                return self.palindrome(s,i+1,j) or self.palindrome(s,i,j-1)
            i += 1
            j -= 1
        return True
    def palindrome(self,s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True