# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node,prev):
            if not node:
                return prev
            right = helper(node.right,prev)
            node.val += right
            prev = node.val
            if node.left:
                prev = helper(node.left,prev)
            return prev
            
        helper(root,0)
        return root