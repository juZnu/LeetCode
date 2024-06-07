
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []

        for intervals in schedule:
            result.extend(intervals)
                
        result.sort(key = lambda x: (x.start,x.end))
        carryResult = []

        for ele in result:
            if not carryResult or carryResult[-1].end < ele.start:
                carryResult.append(ele)
            else:
                carryResult[-1].end = max(ele.end,carryResult[-1].end )

        result = [Interval(float('-inf'),float('inf'))]
        
        for ele in carryResult:
            tmp = result[-1].end
            result[-1].end = ele.start
            result.append(Interval(ele.end,tmp))

        return result[1:-1]
