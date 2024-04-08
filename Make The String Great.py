def makeGood(self, s: str) -> str:
    if not s: return s
    prev = ord(s[0])
    for i in range(1,len(s)):
        pres = ord(s[i])
        if abs(prev - pres) == 32:
            return self.makeGood(s[:i-1]+s[i+1:])
        prev = pres
    return s