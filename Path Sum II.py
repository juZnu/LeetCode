# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append([root,root.val,[root.val]])
        while queue:
            node,sumPath,sumArray = queue.popleft()
            if not(node.left or node.right):
                if sumPath == targetSum:
                    result.append(sumArray)
            else:
                if node.left:
                    queue.append([node.left,sumPath+node.left.val,sumArray + [node.left.val]])
                if node.right:
                    queue.append([node.right,sumPath+node.right.val,sumArray + [node.right.val]])
        return result