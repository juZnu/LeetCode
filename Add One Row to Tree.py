# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root)

        k = 1
        present = [root]

        while depth-1 != k:
            carry = []
            while present:
                ele = present.pop()
                if ele.left:
                    carry.append(ele.left)
                if ele.right:
                    carry.append(ele.right)
            present = carry
            k += 1
        
        for ele in present:
            ele.left = TreeNode(val,ele.left)
            ele.right = TreeNode(val,None,ele.right)
            
        return root
        