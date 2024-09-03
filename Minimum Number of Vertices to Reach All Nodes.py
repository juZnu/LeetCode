class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        visited = set()

        for i in range(n): visited.add(i)

        for start,end in edges:
            if end in visited:visited.remove(end)
        
        return list(visited)
        
        

        

