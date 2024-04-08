# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        carry = deque([root])
        result = []
        while carry:
            carry2 = deque()
            resultcarry = []
            while carry:
                ele = carry.popleft()
                resultcarry.append(ele.val)
                if ele.left:
                    carry2.append(ele.left)
                if ele.right:
                    carry2.append(ele.right)
            result.append(resultcarry)
            carry = carry2
        return result[::-1]



        