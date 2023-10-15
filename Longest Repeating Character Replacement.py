def characterReplacement( s, k):
    str_count = dict()
    l = 0
    maxf= 0
    for r in range(len(s)):
        str_count[s[r]] = str_count.get(s[r],0) + 1
        maxf = max(maxf,str_count[s[r]])
        if r - l+1 - maxf >k:
            str_count[s[l]] -= 1
            l +=1
    return r - l + 1
        

