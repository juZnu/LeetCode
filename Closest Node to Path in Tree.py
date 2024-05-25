import collections
from collections import deque
def closestNode( n, edges, query):
    
    def shortestPath(start,end):
        if start in memo:
            return memo[start]
        
        if start == end:
            return [start]
        
        visited.add(start)
        result = [start]
        bestResult = []
        
        for node in graph[start]:
            if node  not in visited :
                carry = shortestPath(node,end)
                if carry and carry[-1] == end:
                    bestResult = carry
                    memo[node] = carry
        
        return result + bestResult   
    
    graph = {k:[] for k in range(n)}
    
    for k,v in edges:
        graph[k].append(v)
        graph[v].append(k)
        
    result = []
    
    for ele1,ele2,target in query:
        memo= {}
        
        visited = set()
        path1 = shortestPath(ele1,target)
        visited = set()
        path2 = shortestPath(ele2,target)
        
        ele = 0
        
        while path1 and path2 and path1[-1] == path2[-1]:
            ele = path1[-1]
            path1.pop()
            path2.pop()
            
        result.append(ele)
        
    return result

print(closestNode(n = 7, edges = [[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]], query = [[5,3,4],[5,3,6]]))