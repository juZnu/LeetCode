def isAnagram( s, t):
        if  len(s) != len(t):
            return False
        dict_s = dict()
        dict_t = dict()
        for i,j in zip(s,t):
            if dict_s.get(i,0):
                dict_s[i] += 1
            else:
                dict_s[i] = 1
            if dict_t.get(j,0):
                dict_t[j] += 1
            else:
                dict_t[j] = 1   
        return dict_s == dict_t
