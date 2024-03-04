"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        visited = set()
        hashmap = {}
        def dfs(node):
            if node and  node.val not in visited:
                visited.add(node.val)
                print(visited)
                hashmap[node.val] = [nodechild.val for nodechild in node.neighbors]
                for nodechild in node.neighbors:
                    dfs(nodechild)
        dfs(node)
        nodeMap = { k:Node(k) for k,v in hashmap.items()}
        for k,v in hashmap.items():
            for ele in v:
                nodeMap[k].neighbors.append(nodeMap[ele])
        return nodeMap[node.val] if node else node

        

        