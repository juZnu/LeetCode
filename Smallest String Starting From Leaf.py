# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        res = []

        def lexical(array1,array2):
            
            for i in range(-1,-min(len(array1),len(array2))-1,-1):
                if array1[i] > array2[i]:
                    return array2
                elif array1[i] < array2[i]:
                    return array1
            return array1 if len(array1) < len(array2) else array2

        def helper(node,array):
            array.append(node.val)
            if (not node.left) and (not node.right):
                nonlocal res
                if not res:
                    res = array.copy()
                else:
                    res = lexical(res,array.copy())


            if node.left: helper(node.left,array)
            if node.right: helper(node.right,array)
            array.pop()

        if root: helper(root,[])
        print(res)
        res = [chr(ord('a')+ele) for ele in res[::-1]]

        return ''.join(res)


        