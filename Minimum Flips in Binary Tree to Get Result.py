from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        def dfs(result, node):
            if not (node.left or node.right):
                if result == node.val:
                    return 0
                if result != node.val:
                    return 1

            if node.val == 5:
                one = dfs(1, node.left if node.left else node.right)
                zero = dfs(0, node.left if node.left else node.right)
                if result:
                    return zero
                else:
                    return one

            oneLeftCount = dfs(1, node.left) 
            oneRightCount = dfs(1, node.right)
            zeroLeftCount = dfs(0, node.left) 
            zeroRightCount = dfs(0, node.right)

            one_one = oneLeftCount + oneRightCount
            one_zero = oneLeftCount + zeroRightCount
            zero_one = zeroLeftCount + oneRightCount
            zero_zero = zeroRightCount + zeroLeftCount

            if node.val == 2:
                if result:
                    return min(one_zero, zero_one, one_one)
                else:
                    return zero_zero
            elif node.val == 3:
                if result:
                    return one_one
                else:
                    return min(one_zero, zero_one, zero_zero)
            elif node.val == 4:
                if result:
                    return min(zero_one, one_zero)
                else:
                    return min(zero_zero, one_one)

        return dfs(result, root) 

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Test case
nodes = [5, 1, None, None, None]
result = False
root = build_tree(nodes)

solution = Solution()
output = solution.minimumFlips(root, result)
print(f"Minimum flips to get result {result}: {output}")
