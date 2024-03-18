class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for ele in s:
            if ele == t[i]:
                i += 1 
                if i == len(t):
                    return 0
        return len(t[i:])