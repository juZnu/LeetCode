def isIsomorphic( s, t):
    i = 1
    hashmap_s ,hashmap_t = dict(),dict()
    for  char_s,char_t in zip(s,t):
        if (not hashmap_s.get(char_s,0)) and (not hashmap_t.get(char_t,0)) :
            hashmap_s[char_s] = i
            hashmap_t[char_t] = i
            i += 1
        elif not (hashmap_s.get(char_s,0) == hashmap_t.get(char_t,-1)):
            return False
    return True