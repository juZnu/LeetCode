def findAnagrams( s, p):
    rollingHashP = 0
    rollingHashs = 0
    result =[]
    if len(s) >= len(p):
        for i in range(len(p)):
            rollingHashP += ord(p[i]) * hash(p[i])
            rollingHashs += ord(s[i]) * hash(s[i])
        index = 0
        if rollingHashP == rollingHashs :
            result.append(index) 
        for i in range(len(p),len(s)):
            rollingHashs +=  (ord(s[i]) * hash(s[i]))-(ord(s[index]) * hash(s[index]))
            index += 1
            if rollingHashP == rollingHashs:
                result.append(index)
    return result
print(findAnagrams(s = "abab", p = "ab"))