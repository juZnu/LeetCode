from typing import List


def countCompleteComponents( n: int, edges: List[List[int]]) -> int:
    adj = [0 for i in range(n)]
    UF =[-1 for i in range(n)]

    def parent(index):
        if UF[index] < 0:return index
        UF[index] = parent(UF[index])
        return UF[index]
    
    def addUnion(index1,index2):
        parent1 = parent(index1)
        parent2 = parent(index2)
        if parent1 == parent2: return
        if UF[parent1] > UF[parent2]:
            UF[parent1] += UF[parent2]
            UF[parent2] = parent1
        else:
            UF[parent2] += UF[parent1]
            UF[parent1] = parent2

    for edge1,edge2 in edges:
        adj[edge1] += 1
        adj[edge2] += 1
        addUnion(edge1,edge2)

    
    for node in range(n):
        parent(node)

    carry = {}

    for node in range(n):
        parent_node = UF[node]
        if parent_node >= 0:
            if UF[node] not in carry:carry[parent_node] = [] 
            carry[parent_node].append(node)
        elif node not in carry:
            carry[node] = []
            

    res = 0

    for node,neighbours in carry.items():
        length = (UF[node] +1) * (-1)
        cond = True
        for item in neighbours:
            cond = cond and (True if adj[item] == length else False)
        if cond: res += 1
        
    return res


print(countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))