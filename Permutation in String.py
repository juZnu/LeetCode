def checkInclusion( s1, s2):
    dict_s1 = dict()
    for i in s1:
        dict_s1[i] = dict_s1.get(i,0) + 1
    l = 0
    r = 0
    while r - l < len(s1) :
        if dict_s1.get(s2[r],0):
            dict_s1[s2[r]] -= 1
            r += 1
            continue
        while l <r :
            dict_s1[s2[l]] = dict_s1.get(s2[l],0) + 1
            l += 1
    return dict_s1
            
        

print(checkInclusion( "adc",  "dcda"))