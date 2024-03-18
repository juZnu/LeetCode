class Solution(object):
    def checkString(self, s):
        index = s.find('b')
        if index == -1:
            return True
        for ele in s[index:]:
            if ele == 'a':
                return False
        return True





        
        