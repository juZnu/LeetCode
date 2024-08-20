class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        result =[]
        for i in range(len(intervals)):
            start,end = intervals[i]
            while result and ( result[-1][0] <= start <= result[-1][1] or start <= result[-1][0] <= end ):
                carry_start,carry_end = result.pop()
                start = min(start,carry_start)
                end = max(end,carry_end)
            result.append([start,end])
        
        return result