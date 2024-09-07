# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inOrderHashmap = {val:i for i,val in enumerate(inorder)}
        n = len(inorder)

        def Tree(inOrderstart,inOrderEnd,postOrderStart,postOrderEnd):
            if inOrderstart > inOrderEnd or postOrderStart > postOrderEnd:
                return None
            
            node = TreeNode(postorder[postOrderEnd])
            inOrderIndex = inOrderHashmap[node.val]
            left_tree = inOrderIndex - inOrderstart
            node.left = Tree(inOrderstart , inOrderIndex - 1 , postOrderStart , postOrderStart + left_tree - 1)
            node.right = Tree(inOrderIndex + 1 , inOrderEnd , postOrderStart + left_tree  , postOrderEnd - 1)

            return node

        return Tree(0,n-1,0,n-1)