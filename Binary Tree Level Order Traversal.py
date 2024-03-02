# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        result = []
        queue = deque([root,None])
        while queue and root:
            carry = []
            while queue[0]:
                curr = queue.popleft()
                carry.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(carry)
            cur = queue.popleft()
            if queue:
                queue.append(None)
        return result

        

