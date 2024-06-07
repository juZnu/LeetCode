from typing import List


def sumOfDistancesInTree( n: int, edges: List[List[int]]) -> List[int]:
    graph = {k:[] for k in range(n)}

    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)

    memo = {}
    def dfs(i,j):
        if i == j:
            return 0
        stack.add(i)
        
        if (i,j) in memo:
            return memo[(i,j)]
        res = float('inf')
        for v in graph[i]:
            if v not in stack:
                res = min(res, dfs(v,j))
        if res != float('inf'):
            memo[(i,j)] = 1 + res
            memo[(j,i)] = 1 + res
        stack.remove(i)
        return 1 +res
        
            
    result = []
    
    for i in range(n):
        count = 0
        for j in range(n):
            if i!=j :
                stack = set()
                count += dfs(i,j)
        result.append(count)
            
    return result

print(sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))