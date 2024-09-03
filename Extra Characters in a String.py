class Trie:
    def __init__(self):
        self.hashmap = {}
    
    def addWord(self,word):
        carry = self.hashmap
        for char in word:
            if char not in carry:
                carry[char] = {}
            carry = carry[char]
        carry[''] = True
    
    def getWords(self,string):
        res = []
        carry = self.hashmap

        for i in range(len(string)):
            if string[i] not in carry:
                break
            carry = carry[string[i]]
            if carry.get('',False): 
                res.append(i)

        return res

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 0

            res = 1 + dfs(i + 1)

            words = trie.getWords(s[i:])

            for index in words:
                res = min(res,dfs(i+index+1))

            memo[i] = res

            return memo[i]

        return dfs(0)


            
            


        


        