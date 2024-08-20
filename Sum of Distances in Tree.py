import heapq
from typing import List


def sumOfDistancesInTree( n: int, edges: List[List[int]]) -> List[int]:
    graph = {k:{} for k in range(n)}

    for i,j in edges:
        graph[i][j] = 1
        graph[j][i] = 1

    def Dijkstra(node):
        pq =[(0,node)]
        min_dist = {node:0}

        while pq:
            cur_dist,cur_node = heapq.heappop(pq)
            if min_dist.get(cur_node,float('inf')) < cur_dist:
                continue
            for next_node,next_dist in graph[cur_node].items():
                distance = cur_dist + next_dist
                if distance < min_dist.get(next_node, float('inf')):
                    min_dist[next_node] = distance
                    heapq.heappush(pq, (distance, next_node))

        return min_dist

    result = []
    for node in range(n):
        graph[node] = Dijkstra(node)
        carry = 0
        
        for k,v in graph[node].items():
            carry += v
        result.append(carry)

    return result
            


            

print(sumOfDistancesInTree( n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))