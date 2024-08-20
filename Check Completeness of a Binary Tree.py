# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append(root)
        none_found = False
        while queue:
            node = queue.popleft()
            if not node:
                none_found = True
                continue
            else:
                if none_found :
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True



            

        