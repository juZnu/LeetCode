# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        def maxnum(root: Optional[TreeNode]):
            if not root.left and not root.right:
                return TreeNode(root.val)
            root.right =  maxnum(root.right) if root.right else TreeNode(float('-inf'))
            root.left =  maxnum(root.left) if root.left else TreeNode(float('-inf'))
            maxele = max(root.right.val,root.left.val)
            self.result = max(self.result, maxele,root.val+maxele , root.val+root.right.val+root.left.val)
            return TreeNode(max(maxele+root.val,root.val))
        maxele = maxnum(root)
        return self.result

            
        
        
        