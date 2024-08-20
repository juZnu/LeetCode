import collections
import heapq
from typing import List


def countPaths( n: int, roads: List[List[int]]) -> int:
    graph = collections.defaultdict(dict)
    for start,end,wt in roads:
        graph[start][end] = wt
        graph[end][start] = wt
    

    def Dijkstra(node):
        queue = []
        queue.append((0,node))

        min_dist  = {node:0}


        while queue:
            cur_dist,cur_node = heapq.heappop(queue)

            if min_dist.get(cur_node,float('inf')) < cur_dist:
                continue
            
            for next_node,next_dist in graph[cur_node].items():
                calc_dist = cur_dist+next_dist
                if calc_dist < min_dist.get(next_node,float('inf')):
                    min_dist[next_node] = calc_dist
                    if next_node == n-1:res[0] = 1
                    heapq.heappush(queue,(calc_dist,next_node))
                elif next_node == n-1 and calc_dist == min_dist[next_node]:
                    res[0] += 1
            
        return min_dist
    
    res = [0]

    Dijkstra(0)

    return res[0]

print(countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))