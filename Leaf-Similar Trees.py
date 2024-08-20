# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def helper(node):
            result =[]
            if not node.left and not node.right:
                return [node.val]
            result += helper(node.left) if node.left else []
            result += helper(node.right) if node.right else []
            return result

        
        return helper(root1) == helper(root2)
