# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res =root.val
        queue = []
        if root:queue.append(root)
        while queue:
            carry = []
            res = queue[0].val
            for node in queue:
                if node.left:
                    carry.append(node.left)
                if node.right:
                    carry.append(node.right)
            queue = carry
        return res