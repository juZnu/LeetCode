from typing import List


def longestPalindrome(self, words: List[str]) -> int:
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word,0) + 1
        
        res = 0
        center =False
        for word,count in hashmap.items():
            if word[0] == word[1]:
                div,mod = divmod(count,2)
                res += div*4
                if mod : center = True
            elif hashmap.get(word[::-1],0):
                res += min(hashmap[word],hashmap[word[::-1]])*4
                hashmap[word[::-1]] = 0
            hashmap[word] = 0

        return res + (2 if center else 0)