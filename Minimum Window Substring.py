def minWindow( s, t):
        if len(t) >len(s):
            return ''
        dict_t = dict()
        dict_s = dict()
        for i in t:
            dict_t[i] = dict_t.get(i,0) + 1
            dict_s[i] = 0
        result = float('infinity')
        result_i = []
        count = 0
        l = 0
        for r in range(len(s)):
            if dict_t.get(s[r],0):
                dict_s[s[r]] += 1
                count += 1 if dict_s[s[r]] <= dict_t[s[r]] else 0
            while count == len(t):
                if r-l+1 < result:
                    result = r-l+1
                    result_i = [l,r+1]
                if dict_t.get(s[l],0):
                    dict_s[s[l]] -= 1
                    count -= 1 if dict_s[s[l]] < dict_t[s[l]] else 0
                l += 1
        return '' if result == float('infinity') else s[result_i[0]:result_i[1]]


print(minWindow(s = "ADOBECODEBANC", t = "ABC"))