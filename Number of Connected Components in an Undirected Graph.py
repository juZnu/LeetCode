class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = [-1 for _ in range(n)]
        def parent(index):
            if UF[index] < 0:
                return index
            UF[index] = parent(UF[index])
            return UF[index] 
        
        def union(index1, index2):
            parent1, parent2 = parent(index1),parent(index2)
            if parent1 == parent2:  return False
            elif UF[parent1] > UF[parent2]:
                UF[parent1] +=UF[parent2]
                UF[parent2] = parent1
            else:
                UF[parent2] +=UF[parent1]
                UF[parent1] = parent2
            return True

        for index1,index2 in edges:
            union(index1,index2)

        connected = 0

        for ele in UF:
            if ele <0:
                connected += 1

        return connected

