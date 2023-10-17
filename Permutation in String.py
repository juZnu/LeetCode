def checkInclusion( s1, s2):
    dict_s1 = dict()
    for i in s1:
        dict_s1[i] = dict_s1.get(i,0) + 1
    l = 0
    r = 0
    while  r + len(s1) <=len(s2):
        dict_s2 = dict()
        for i in range(len(s1)):
            if not dict_s1.get(s2[r+i],0):
                break
            dict_s2[s2[r+i]] = dict_s2.get(s2[r+i],0) + 1
        if dict_s1 == dict_s2:
            return True
        r =l+1
        l += 1
    return False

