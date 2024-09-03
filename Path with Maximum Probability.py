class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            start,end = edges[i]
            prob = succProb[i]
            graph[start].append([end,prob])
            graph[end].append([start,prob])

        max_heap = [(-1.0,start_node)]
        node_prob = [0.0 for _ in range(n)]
        node_prob[start_node] =1.0

        while max_heap:
            prob,node = heapq.heappop(max_heap)
            prob = -prob
            if node_prob[node] > prob:continue
            node_prob[node] = prob
            for next_node,next_prob in graph[node]:
                cont_prob = next_prob * prob
                if cont_prob  > node_prob[next_node]:
                    heapq.heappush(max_heap,(-cont_prob,next_node))  

        return node_prob[end_node]      
        
        
