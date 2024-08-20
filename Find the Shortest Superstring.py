from typing import List


def shortestSuperstring(words: List[str]) -> str:
    def score(str1,str2):
            for i in range(len(str1)):
                length = len(str1[i:])
                if str1[i:] == str2[:length]:return length
            return 0

    adj = []
    hashmap = {}
    for i in range(len(words)):
        carry = []
        for j in range(len(words)):
            if i == j:carry.append(float('inf'))
            else:carry.append(score(words[i],words[j]))
        hashmap[words[i]] = i
        adj.append(carry)
    
    length = float('inf')
    
    return ""

print(shortestSuperstring(words = ["catg","ctaagt","gcta","ttca","atgcatc"]))