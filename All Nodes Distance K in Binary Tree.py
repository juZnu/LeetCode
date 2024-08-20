# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def createGraph(node):
            if not (node.left or node.right):return 

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                createGraph(node.right)

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                createGraph(node.left)
        
        def dfs(node,count):
            
            if not count:
                result.append(node)
                return

            visited.add(node)

            for next_node in graph[node]:
                if next_node not in visited:
                    dfs(next_node,count-1)

            visited.remove(node)
        
        graph = collections.defaultdict(list)
        result = []
        visited = set()

        createGraph(root)


        dfs(target.val,k)
        
        return result
            
            

                




        