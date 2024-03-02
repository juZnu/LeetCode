# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sameTree(self,tree1,tree2):
        if not tree1 and not tree2:
            return True
        elif tree1 and tree2 and tree1.val == tree2.val:
            return self.sameTree(tree1.left,tree2.left) and self.sameTree(tree1.right,tree2.right)
        return False

    def isSubtree(self, s, t):
        if not t:
            return True
        if not s:
            return False
        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)