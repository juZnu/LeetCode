class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result= ''
        i = 0
        while word1[i:] and word2[i:]:
            result += word1[i]+word2[i]
            i += 1
        return result + (word1[i:] or word2[i:])
        