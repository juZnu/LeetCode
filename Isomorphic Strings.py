class Solution(object):
    def isIsomorphic(self, s, t):
        i = 1
        hashmap_s ,hashmap_t = dict(),dict()
        for  char_s,char_t in zip(s,t):
            if  hashmap_s.get(char_s,0) ==  hashmap_t.get(char_t,0) :
                hashmap_s[char_s] = i
                hashmap_t[char_t] = i
                i += 1
            else:
                return False
        return True
        