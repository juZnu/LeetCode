# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and root.val > high:
            root = root.left
        
        while root and root.val < low:
            root = root.right
        
        if not root:
            return 

        if not (low <= root.val <= high):
            return self.trimBST(root,low,high)

        parent = root
        left = root.left if root else None

        while left:
            if left.val < low:
                left.left = None
                parent.left = left.right
                left = parent.left
                continue
            parent = left
            left = left.left
        
        parent = root
        right = root.right if root else None

        while right:
            if right.val > high:
                right.right = None
                parent.right = right.left
                right = parent.right
                continue
            parent = right
            right = right.right
            
        

        return root

