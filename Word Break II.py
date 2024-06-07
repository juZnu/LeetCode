from typing import List


def wordBreak( s: str, wordDict: List[str]) -> List[str]:
    wordDict = set(wordDict)
    res = []
    
    def helper(i,carry):
        if i == len(s):
            res.append(carry)
            
            
        for j in range(i,len(s)):
            if s[i:j+1] in wordDict:
                carry.append(s[i:j+1])
                helper(j+1,carry.copy())
                carry.pop()
                
    helper(0,[])
    return res
    
    
print(wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))