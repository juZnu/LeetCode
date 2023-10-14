def groupAnagrams(strs):
    result= dict()
    for word in strs:
        key = [0]*26
        for letter in word:
            key[ord(letter)-97] += 1
        key = tuple(key)
        if result.get(key,0):
            result[key]+=[word]
        else:
            result[key] = [word]
    return result.values()