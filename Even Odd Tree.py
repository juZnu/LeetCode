# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        if root:
            queue.append(root)
        odd = True
        
        while queue:
            prev = float('-inf') if odd else float('inf')
            carry = []
            for node in queue:
                if odd:
                    if (not node.val%2) or prev >= node.val :
                        return False
                else:
                    if (node.val%2) or prev <= node.val:
                        return False
                
                if node.left:carry.append(node.left)
                if node.right: carry.append(node.right)
                
                prev = node.val
            queue = carry
            odd = not odd

        return True
        