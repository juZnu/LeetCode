import collections
from typing import List
import heapq

def minimumWeight( n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    graph = {i:{} for i in range(n)}

    for src,dst,wt in edges:
        graph[src][dst] = min(graph.get(src,{}).get(dst,float('inf')),wt)
    
    def Djkstra(node):
        queue = [(0,node)]
        min_cost ={node:0}
        while queue:
            cur_wt,cur_node = heapq.heappop(queue)
            if cur_wt > graph[node].get(cur_node,float('inf')):
                continue
            for next_node,next_wt in graph[cur_node].items():
                wt = cur_wt+next_wt 
                if wt < min_cost.get(next_node,float('inf')):
                    min_cost[next_node] = wt
                    heapq.heappush(queue,(wt,next_node))
        
        return min_cost
    for i in range(n):
        graph[i] = Djkstra(i)
    
    print(graph)
    return 0
    
    


print(minimumWeight(n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5))