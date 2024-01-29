def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and i+len(needle) < len(haystack)+1:
            found = True
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    found = False
                    break
            if found:
                 return i
    return -1   
print(strStr(haystack = "abc", needle = "c"))