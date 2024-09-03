import collections
from typing import List


def minReorder( n: int, connections: List[List[int]]) -> int:
    array = [_ for _ in range(n)]
    res = 0
    connections = collections.deque(connections)
    while connections:
        start,end = connections.popleft()
        if not start or not array[start]:
            res += 1
            start,end = end,start
        if not end or not array[end]:
            array[start] = 0
        else:
            connections.append([start,end])
        
    return res

print(minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))