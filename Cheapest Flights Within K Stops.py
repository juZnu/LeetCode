class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))
        
        memo = {}

        def dfs(node, step): 

            if (node,step) in memo: return memo[(node,step)] 
            if node == dst: return 0      
            if not step: return float('inf')
    
            minCost = float('inf')

            for neighbour, price in graph[node]:
                currentCost = price + dfs(neighbour, step - 1)
                minCost = min(minCost,currentCost)

            memo[(node,step)] = minCost

            return minCost
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1