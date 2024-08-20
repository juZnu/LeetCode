class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        
        for index in range(len(rating)):
            lg,rs = 0,0
            ls,rg = 0,0
            for l in range(index):
                if rating[l] > rating[index]:
                    lg += 1
                elif rating[l] < rating[index]:
                    ls += 1
            for r in range(index+1,len(rating)):
                if rating[r] > rating[index]:
                    rg += 1
                elif rating[r] < rating[index]:
                    rs += 1
            res += (lg*rs) + (ls*rg)

        return res


        