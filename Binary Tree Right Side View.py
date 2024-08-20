# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque()
        if root:queue.append(root)
        while queue:
            result.append(queue[-1].val)
            carry = collections.deque()
            while queue:
                ele = queue.popleft()
                if ele.left: carry.append(ele.left)
                if ele.right: carry.append(ele.right)
            queue = carry
        return result
        