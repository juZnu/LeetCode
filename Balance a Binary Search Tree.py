# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inOrderTraversal(node):
            if not node: return []
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right)

        def sortArrayBST(array):
            if not array: return None
            midLength = len(array)//2
            return TreeNode(array[midLength],sortArrayBST(array[:midLength]),sortArrayBST(array[midLength+1:]))
        
        return sortArrayBST(inOrderTraversal(root))
        