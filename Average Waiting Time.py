class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        time = 0 
        for entry,prep in customers:
            if entry > time:time = entry
            time = time+prep
            res += time - entry

        return res / len(customers)