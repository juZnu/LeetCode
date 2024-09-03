# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def palindrome(hashmap):
            carry = 0
            for k,v in hashmap.items():
                carry += v%2

            return carry <= 1
        
        hashmap =set()

        res = [0]

        def helper(node,hashmap):

            if node.val in hashmap:
                hashmap.remove(node.val)
            else:
                hashmap.add(node.val)

            if (not node.left) and (not node.right):
                if len(hashmap) <2 :res[0] += 1
            
            if node.left:helper(node.left,hashmap)
            if node.right:helper(node.right,hashmap)

            if node.val in hashmap:
                hashmap.remove(node.val)
            else:
                hashmap.add(node.val)
            

        if root:
            helper(root,hashmap)

        return res[0]