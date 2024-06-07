def equalSubstring( s: str, t: str, maxCost: int) -> int:
    l = 0
    k = maxCost
    res = 0
    for r in range(len(s)):
        k -= abs(ord(s[r])- ord(t[r]))
        while k < 0 and l<=r:
            k += abs(ord(s[l])- ord(t[l]))
            l += 1
        res = max(res,r-l+1)
    return res

print(equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19))