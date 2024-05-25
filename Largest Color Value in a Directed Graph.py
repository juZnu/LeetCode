class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        memo = {}
        def dfs(node,hashmap):
            if node in stack:
                return {}

            if node in memo:
                return memo[node]
                
            stack.add(node)
            
            for point in graph.get(node,[]):
                memo[point] = dfs(point,hashmap.copy())
                if not memo[point]:
                    return {}
                
            if node in graph:
                for k,v in hashmap.items():
                    hashmap[k] = max([memo[point][k] for point in graph[node]]+[v])
                    
            hashmap[colors[node]] += 1
            stack.remove(node)
            return hashmap
            
                
        graph = {}
        for k,v in edges:
            if not graph.get(k,0):
                    graph[k] = []
            graph[k].append(v)

        stack = set()

        map = {k : 0 for k in set(colors)}
        result = [1]

        for key in graph.keys():
            if key not in memo:
                memo[key] = dfs(key,map.copy())
                if memo[key]:
                    result[0] = max(result[0], max(memo[key].values()))
                else:
                    return -1

        return result[0] if result[0] != float('inf') else -1 