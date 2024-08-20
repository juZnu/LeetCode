class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        begin, end  = 1,1
        n = 0
        while not(begin <= label <= end):
            begin,end = end,begin
            n += 1
            begin += 1
            end = begin-1 + (1<<n) 
 
        res = [label]
        while label >1:
            label = begin+end -label 
            label //= 2
            res.append(label)
            begin = begin//2
            end  = end//2
        return res[::-1]



        
        