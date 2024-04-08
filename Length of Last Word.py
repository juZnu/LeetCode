def lengthOfLastWord(self, s: str) -> int:
    r = len(s) -1
    while r > -1 and s[r]== ' ':
        r -= 1
    l = r
    while l > -1 and s[l] != " ":
        l -= 1
    return r-l