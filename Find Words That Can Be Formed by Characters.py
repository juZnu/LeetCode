class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        hashmap = collections.Counter(chars)
        for word in words:
            cond = True
            carryMap = collections.defaultdict(int)
            for char in word:
                carryMap[char] += 1
                if carryMap[char] > hashmap[char]:
                    cond = False
                    break
            if cond:
                res += len(word)
        return res