# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree( preorder, inorder):
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    n = len(preorder)
    
    def Tree( preOrderStart,preOrderEnd , inOrderStart,inOrderEnd):
        if preOrderStart > preOrderEnd or inOrderStart > inOrderEnd:
            return None
        
        root = TreeNode(preorder[preOrderStart])
        
        inOrderIndex = inorder_map[root.val]
        
        newPreOrderEnd = inOrderIndex - inOrderStart
        
        root.left = Tree( preOrderStart+1,newPreOrderEnd , inOrderStart,inOrderIndex-1)
        root.right = Tree( newPreOrderEnd+1,preOrderEnd , inOrderIndex+1,inOrderEnd)
        
        return root
        
    return Tree(0,n-1,0,n-1)
        
print(buildTree([1,2,3,4],[1,2,3,4]))