def countPalindromicSubsequence(s):
    result = 0
    first = dict()
    last = dict()
    for i in range(len(s)):
        if first.get(s[i],-1) == -1:
            first[s[i]] = i
        last[s[i]] = i
    for k,v in first.items():
        if last.get(k,-1) >-1  and  last.get(k,0)- v >=2:
            result += len(set(s[v+1:last[k]]))
    return result