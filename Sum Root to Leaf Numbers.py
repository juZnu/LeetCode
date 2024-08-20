# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def helper(node,prev):
            carry = (prev*10) + node.val
            if not node.left and not node.right:
                res[0] += carry
                return
            if node.right:
                helper(node.right,carry)
            if node.left:
                helper(node.left,carry)
        helper(root,0)
        return res[0]
        