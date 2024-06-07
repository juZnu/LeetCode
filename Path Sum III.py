# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = [0]
        hashSet = collections.defaultdict(int)

        def traversal(node,carrySet,carrySum):
            if not node:
                return

            carrySum += node.val
            result[0] += carrySet[carrySum - targetSum]

            carrySet[carrySum] += 1
            traversal(node.left,carrySet,carrySum)
            traversal(node.right,carrySet,carrySum)
            carrySet[carrySum] -= 1
            
        hashSet[0] = 1
        traversal(root,hashSet,0)

        return result[0]
        