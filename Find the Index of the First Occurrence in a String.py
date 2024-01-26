def strStr(haystack, needle):
    length = len(needle)
    for i in range(len(haystack)):
        if i+length > (len(haystack)-1):
            break
        elif haystack[i] == needle[0]:
            boolean = True
            for j in range(length):
               if  haystack[i+j] != needle[j]:
                   boolean = False
                   break
            if boolean:
                return i
    return -1
print(strStr(haystack = "a", needle = "a"))