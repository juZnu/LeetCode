"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def QuadTree(r1,r2,c1,c2):
            if c1 == c2 and r1 == r1:
                return Node(grid[r1][c2],True,None,None,None,None)
            mid_r = r1 + (r2-r1)//2
            mid_c =  c1 + (c2-c1)//2
            topLeft = QuadTree(r1,mid_r,c1,mid_c)
            topRight = QuadTree(r1,mid_r,mid_c+1,c2)
            bottomLeft = QuadTree(mid_r+1,r2,c1,mid_c)
            bottomRight = QuadTree(mid_r+1,r2,mid_c+1,c2)
                

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        
        return QuadTree(0,len(grid)-1,0,len(grid)-1)