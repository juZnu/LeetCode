import bisect
import heapq
from typing import List


def minRefuelStops( target: int, startFuel: int, stations: List[List[int]]) -> int:
    res = 0
    stations.sort()
    entry = (-startFuel,0)
    pq =[(-startFuel,0)]
    i = 0
    while i < len(stations):
        stop,fuel = stations[i]

        if stop <= startFuel:
            heapq.heappush(pq,( -(fuel+ (startFuel)) , stop))
            i += 1

        elif pq:
            nextFuel,nextStop =heapq.heappop(pq)
            nextFuel = -nextFuel
            if nextFuel >= target:return res+1
            pq = []
            i = bisect.bisect(stations,[nextStop,nextFuel+nextStop-startFuel])
            startFuel =nextFuel
            res += 1
            
        else:
            return -1
    ele = heapq.heappop(pq)
    if ele == entry: return res
    return res+1 if -ele[0] >= target else -1
print(minRefuelStops(1000,299,[[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]))