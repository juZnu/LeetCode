from typing import List


def findCheapestPrice( n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[float('inf') for _ in range(n)] for i in range(n) ]
    for src,dest,price in flights:
        graph[dest][src] = price
    
    return


print(findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))        
