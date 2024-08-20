# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(node,prevSum):
            if not node:
                return prevSum
            prevSum = helper(node.right,prevSum)
            node.val += prevSum
            prevSum = node.val
            return helper(node.left,prevSum)


        helper(root,0)
        return root

        