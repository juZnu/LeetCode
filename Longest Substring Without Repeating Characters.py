def lengthOfLongestSubstring(s):
    i = 0
    j = 0
    result =0
    while j <len(s):
        if s[j] in s[i:j]:
            result = max(result,j-i)
            i = j
            while s[i-1] != s[j]:
                i -= 1
            continue
        j+= 1
    return max(result,j-i)