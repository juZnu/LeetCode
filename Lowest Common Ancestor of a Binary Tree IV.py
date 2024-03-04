# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        nodes = set(nodes)
        
        def dfs(root,nodes):
            
            if not root:
                return None
            
            if root in nodes:
                return root
            l = dfs(root.left,nodes)
            r = dfs(root.right,nodes)
            if l and r:
                return root
            else:
                return l or r
        return dfs(root,nodes)
        