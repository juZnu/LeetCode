class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target): return -1

        adj = [[float('inf') if i!=j else 0 for j in range(26)] for i in range(26)]

        for value1,value2,cost_value in zip(original,changed,cost):
            adj[ord(value1)-ord('a')][ord(value2)-ord('a')] = min(adj[ord(value1) - ord('a')][ord(value2) - ord('a')], cost_value)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if adj[i][j] > adj[i][k] + adj[k][j]:
                        adj[i][j] = adj[i][k] + adj[k][j]
        
        res = 0
        for value1,value2 in zip(source,target):
            res += adj[ord(value1)-ord('a')][ord(value2)-ord('a')]

        return res if float('inf') !=  res else -1
                    

        

        



            