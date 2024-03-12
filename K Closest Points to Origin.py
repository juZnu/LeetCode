import heapq
from typing import List
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    points = [((x**2)+(y**2),[x,y]) for x,y in points]
    heapq.heapify(points)
    result = []
    while k:
        ele = heapq.heappop(points)
        result.append(ele[1])
        k -= 1
    return result