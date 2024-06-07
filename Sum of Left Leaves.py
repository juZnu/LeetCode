# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        def helper(node, isLeft):
            if not node: return

            if not (node.left or node.right ):
                if isLeft: ans.append(node.val)
                return
            
            helper(node.right,False)
            helper(node.left,True)

        helper(root,False)
        return sum(ans)
        