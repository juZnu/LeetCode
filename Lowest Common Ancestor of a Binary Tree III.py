
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        arr1,arr2 = [],[]
        while p:
            arr1.append(p)
            p = p.parent
        
        while q:
            arr2.append(q)
            q = q.parent

        res = None
        while arr1 and arr2:
            if arr1[-1] != arr2[-1]:break
            res = arr1.pop()
            arr2.pop()

        return res
        