from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            i = 0
            j = len(word)-1
            while i<j:
                if word[i]!=word[j]: return False
                i += 1
                j -= 1
            return True

        for ele in words:
            if isPalindrome(ele):return ele
            
        return ''
        