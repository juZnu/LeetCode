# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteLeaf(node,parent):
            if node.right or node.left:return 
            if parent :
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            return

        def helper(node,parent):
            
            if node.left:helper(node.left,node)
            if node.right:helper(node.right,node)

            if node.val == target: deleteLeaf(node,parent)

            return

        helper(root,None)
        
        if root.val == target and (not root.left and not root.right):
            return None
        return root
