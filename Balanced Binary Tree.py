# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True,1
            cond_left,height_left = helper(node.left)
            cond_right,height_right = helper(node.right)
            cond = cond_left and cond_right and abs(height_left - height_right) <= 1
            return cond, 1+max(height_left,height_right)
        cond,height = helper(root)
        return cond
            
        