# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def helper(node,prevMax):
            if not node: return
            if node.val >= prevMax:
                res[0] += 1
                prevMax = node.val
            helper(node.left,prevMax)
            helper(node.right,prevMax)
        
        if root: helper(root,float('-inf'))
        return res[0]
