# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sumRange(node):
            if not node: return  0
            ele  = node.val if low <= node.val <= high else 0
            return sumRange(node.left) + ele + sumRange(node.right)
        return sumRange(root)
        