# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(node):
            if not node: return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        dummy = TreeNode()
        node = dummy
        for ele in inOrder(root):
            node.right = TreeNode(ele)
            node = node.right
        
        return dummy.right

        

        