class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [(int(ele[:2]),int(ele[3:])) for ele in timePoints]
        timePoints.sort()
        result  = float('inf')
        for i in range(1,len(timePoints)):
            time = 0
            time += (timePoints[i][0] - timePoints[i-1][0])*60
            time -= timePoints[i-1][1] - timePoints[i][1] 
            result = min(result,time)

        time = 0
        time += (timePoints[0][0]+24 - timePoints[-1][0])*60
        time -= timePoints[-1][1] - timePoints[0][1]  
        result = min(result,time)
        return result
        