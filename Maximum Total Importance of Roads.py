import heapq
from typing import List


def maximumImportance( n: int, roads: List[List[int]]) -> int:
    degree = [[i,0] for i in range(n)] 
    for start,end in roads:
        degree[start][1] += 1
        degree[end][1] += 1
    
    res = 0
    degree.sort(key=lambda ele: ele[1],reverse=True)
    for node,deg in degree:
        res += (deg*n)
        n -= 1
    
    return res

print(maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))