class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numSet = set()

        for start,end in edges:
            numSet.add(start)
            numSet.add(end)

        UF = [-1 for i in range(len(numSet))]
        res =[]

        def parent(index):
            if UF[index] < 0:
                return index
            return parent(UF[index])
        
        def union(index1, index2):
            parent1, parent2 = parent(index1),parent(index2)
            if parent1 == parent2:  return True
            elif UF[parent1] > UF[parent2]:
                UF[parent1] +=UF[parent2]
                UF[parent2] = parent1
            else:
                UF[parent2] +=UF[parent1]
                UF[parent1] = parent2
            return False
    
        for index1,index2 in edges:
            if union(index1-1,index2-1):
                res = [index1,index2]
        
        return res