def strWithout3a3b( a: int, b: int) -> str:
    def helper(a,b,res):
        if len(res) >=3 and (res[-3:] =='aaa' or res[-3:] =='bbb'):
            return False

        if not a and not b:return res

        res1,res2= False, False

        if a:res1 = helper(a-1,b,res+'a')
        
        if b:res2 = helper(a,b-1,res+'b')

        return res1 or res2
    
    return helper(a,b,'')

print(strWithout3a3b(1,2))