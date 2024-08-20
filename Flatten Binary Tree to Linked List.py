# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def changeTree(node):
            if ((not node.right) and (not node.left) )or not node:
                return node,node
            start = node
            end = node.right
            tmp =node.right
            if node.left:
                start,end =changeTree(node.left)
                node.left = None
                node.right =start
                end.right =tmp
            if tmp:
                start,end = changeTree(tmp)
            
            return node,end
        
        if root and (root.left or root.right) :
            changeTree(root)