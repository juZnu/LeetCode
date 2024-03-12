# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        result = 0
        def maxHeights(root):
            nonlocal result
            if not root: return 0
            left = maxHeights(root.left)
            right = maxHeights(root.right)
            result = max(result, left + right)
            return 1+max(left,right)
        maxHeights(root)
        return result