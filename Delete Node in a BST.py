# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteMinNode(node,parent):
            if not node.left:
                res = node.val
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                return res
            return deleteMinNode(node.left,node)
            
        def findNode(node,parent):
            if not node:
                return 
            if node.val == key:
                if node.right:
                    node.val = deleteMinNode(node.right,node)
                else:
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                
                return 

            findNode(node.left,node)
            findNode(node.right,node)

        dummy = TreeNode('',root)
        findNode(root,dummy)

        return dummy.left


        