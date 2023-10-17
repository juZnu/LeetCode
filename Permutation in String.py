def checkInclusion( s1, s2):
    h1 = 0
    h2 = 0
    for i in range(len(s1)):
        h1 += hash(s1[i])*ord(s1[i])
        h2 += hash(s2[i])*ord(s2[i])
    for i in range(len(s1),len(s2)):
        if h1 == h2:
            return True
        h2 += hash(s2[i])*ord(s2[i]) - (hash(s2[i -len(s1)]) * ord(s2[i - len(s1)]))
    return h1 == h2

