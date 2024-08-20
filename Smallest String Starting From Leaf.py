from typing import Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        maxLength = [float('inf')]
        res = []
        def helper(node,strArray):
            ele = chr(ord('a')+node.val)
            strArray.append(ele)
            if (not node.left) and (not node.right):
                if len(strArray) < maxLength[0]:
                    maxLength[0] = len(strArray)
                    res = strArray.copy()
                return
            if node.left:
                helper(node.left,strArray)
            if node.right:
                helper(node.right,strArray)
            strArray.pop()
        if root:helper(root,[])
        return ''.join(res[::-1])

class TestSolution(unittest.TestCase):
    def test_smallestFromLeaf(self):
        # Creating the binary tree [0,1,2,3,4,3,4]
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        
        solution = Solution()
        result = solution.smallestFromLeaf(root)
        expected_result = "dba"  # Explanation: The path "3->1->0" forms the string "dba"
        
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
