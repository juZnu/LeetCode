from typing import List


def maxRunTime( n: int, batteries: List[int]) -> int:
    import heapq
    pq = [-i for i in batteries]
    heapq.heapify(pq)
    res = 0

    while len(pq) >= n:
        carry = []
        last = 0
        for _ in range(n):
            ele = heapq.heappop(pq)
            if ele:carry.append(ele+1)
        while carry:
            heapq.heappush(pq,carry.pop())

        res += 1  

    return res  

print(maxRunTime(n = 2, batteries = [3,3,3]))