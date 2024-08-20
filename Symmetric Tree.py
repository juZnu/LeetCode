# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        left.append(root.left)
        right.append(root.right)


        while left and right:
            carry_left = []
            carry_right = []
            for node1,node2 in zip(left,right):
                
                if not node1 and not node2:
                    continue
                # If one is None and the other isn't, it's not symmetric
                elif not node1 or not node2:
                    return False
                # If the values don't match, it's not symmetric
                elif node1.val != node2.val:
                    return False
                
                # Add children in mirrored order
                carry_left.append(node1.left)
                carry_left.append(node1.right)
                carry_right.append(node2.right)
                carry_right.append(node2.left)

                
            left,right = carry_left,carry_right
            if len(left) != len(right):
                return False

        return True
            
            