# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            maxValue = float('-inf')
            carry = []
            for node in queue:
                maxValue = max(maxValue,node.val)
                if node.left:
                    carry.append(node.left)
                if node.right:
                    carry.append(node.right)
            queue = carry
            res.append(maxValue)
        return res
        