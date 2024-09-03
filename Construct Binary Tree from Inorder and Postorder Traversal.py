# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTree(inOrder,postOrder):
            if len(inOrder) == 1:
                return TreeNode(inOrder[0])
            elif not inOrder:
                return None
            
            node = TreeNode(postOrder.pop())
            i = 0
            while inOrder[i] != node.val:
                i += 1

            left_inorder = inOrder[:i]
            right_inorder = inOrder[i+1:]
            
            j = len(left_inorder)
            left_postorder = postOrder[:j] if left_inorder else None
            right_postorder = postOrder[j:] if right_inorder else None

            node.left = buildTree(left_inorder,left_postorder) if left_inorder else None
            node.right = buildTree(right_inorder,right_postorder)  if right_inorder else None
            
            return node

        return buildTree(inorder,postorder)