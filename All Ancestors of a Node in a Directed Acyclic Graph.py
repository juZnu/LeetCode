import collections
from typing import List


def getAncestors( n: int, edges: List[List[int]]) -> List[List[int]]:
    graph = dict()
    for start,end in edges:
        if not end in graph: graph[end] = []
        graph[end].append(start)
    result = []
    def dfs(node,visited,ancestor_set):
        if node < len(result):
            return set(result[node])
        for ancestor in graph.get(node,[]):
            if ancestor not in visited:
                visited.add(ancestor)
                ancestor_set.add(ancestor)   
                for ele in dfs(ancestor,visited,ancestor_set):ancestor_set.add(ele)
        return ancestor_set
            
    for i in range(n):
        result.append(sorted(list(dfs(i,set(),set()))))
    return result

print(getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))