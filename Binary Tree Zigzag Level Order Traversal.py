# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        levelOrder = collections.deque()
        if root:levelOrder.append(root)
        zigzag = True
        while levelOrder:
            carryResult = []
            carryOrder = collections.deque()

            while levelOrder:
                ele = levelOrder.popleft()
                carryResult.append(ele.val)
                if ele.left:
                    carryOrder.append(ele.left)
                if ele.right:
                    carryOrder.append(ele.right)
            
            if zigzag:
                result.append(carryResult)
            else:
                result.append(carryResult[::-1])
            zigzag = not zigzag
            levelOrder = carryOrder
            
        return result

        