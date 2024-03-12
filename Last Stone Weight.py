import heapq
from typing import List

def lastStoneWeight( stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones)> 1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        diff = stone1-stone2
        if diff:heapq.heappush(stones,diff)
    return abs(stones[0]) if stones else 0

print(lastStoneWeight(stones = [3,7,2]))