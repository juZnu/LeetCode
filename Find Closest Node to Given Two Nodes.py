from typing import List


def closestMeetingNode( edges: List[int], node1: int, node2: int) -> int:
    path1,path2 = {node1},{node2}
    
    while (node1 not in path2 and node2 not in path1):
        node1 = edges[node1] if node1 != -1 else node1
        node2 = edges[node2] if node2 != -1 else node2
        if (node1  in path1 and node2  in path2):
            break
        
        if node1 not in path1:
            path1.add(node1)
        
        if node2 not in path2:
            path2.add(node2)
            

    res = node1 if node1 in path2 else -1
    if node2 in path1:res = node2
    return res

print(closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))