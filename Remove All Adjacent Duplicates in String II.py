class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        for ele in s:
            if res and res[-1][0] == ele:
                res[-1][1] += 1
            else:
                res.append([ele,1])

            while res and res[-1][1] == k:
                res.pop()
                
        res2 = []
        for ele,count in res:
            res2.append(ele*count)

        return ''.join(res2)


        