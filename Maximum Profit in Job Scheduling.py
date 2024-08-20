class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        schedule = [(x,y,z) for x,y,z in zip(startTime,endTime,profit)]
        schedule.sort(key = lambda x: (x[0]))
        dp = [[i,0] for i,_,_ in schedule]
        
        res = 0
        for i in range(len(schedule)-1,-1,-1):
            start,end,profit = schedule[i]
            endIndex = bisect.bisect_left(dp,[end,0])
            if -1 < endIndex < len(dp):
                profit += dp[endIndex][1]
            res = max(res,profit)
            dp[i][1] = res
        return res