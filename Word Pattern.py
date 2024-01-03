def wordPattern( pattern, s):
    sHash = dict()
    hashPattern = dict()
    s= s.split(' ')
    if len(s) != len(pattern):
        return False
    for val,sVal in zip(pattern,s):
        if sHash.get(val,0) and sHash[val] != sVal:
                return False
        elif hashPattern.get(sVal,0) and hashPattern[sVal] != val:
                return False
        else:
            sHash[val] = sVal
            hashPattern[sVal] =val
    return True
print(wordPattern(pattern = "abba", s= "dog dog dog dog"))