class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getBitMask(word):
            res = 0
            for ele in word:
                res |= 1<<(ord(ele)-ord('a'))
            return res

        res = 0
        bitmask = []

        for word in words:
            bitmask.append([getBitMask(word),len(word)])

        for i in range(len(bitmask)):
            ele1,len1  = bitmask[i]
            for j in range(i+1,len(bitmask)):
                ele2,len2  = bitmask[j]
                if not(ele1 & ele2):
                    res = max(res,len1*len2)

        return res

        