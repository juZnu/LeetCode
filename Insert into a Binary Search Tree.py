# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:return TreeNode(val)
        def helper(node,parent):
            if not node:
                if val > parent.val:
                    parent.right = TreeNode(val)
                else:
                    parent.left = TreeNode(val)
                return

            if node.val < val:
                helper(node.right,node)
            else:
                helper(node.left,node)
            
        helper(root,None)
        return root