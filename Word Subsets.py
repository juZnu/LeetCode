class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hashmap = collections.Counter()
        for b in words2:
            hashmap |= collections.Counter(b)
        
        res = []
        
        for word in words1:
            carry = hashmap.copy()
            for char in word:
                if char in carry:
                    carry[char] -= 1
                    if not carry[char]:del carry[char]
            if not carry:
                res.append(word)
        
        return res
                
        