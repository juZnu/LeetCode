class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = [newInterval]
        for start,end in intervals:
            carry_start,carry_end = result.pop()
            if (carry_start <= start <= carry_end) or (start <= carry_start <= end):
                append_ele = [min(carry_start,start),max(carry_end,end)]
                result.append(append_ele)
            elif end < carry_start:
                result.append([start,end])
                result.append([carry_start,carry_end])
            else:
                result.append([carry_start,carry_end])
                result.append([start,end])
        return result



            

