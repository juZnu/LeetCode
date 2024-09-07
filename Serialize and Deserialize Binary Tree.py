# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    def serialize(self, root):
        def dfs(node):
            if not node:
                return '#'
    
            return dfs(node.right)+','+dfs(node.left)+','+str(node.val)
        return dfs(root)

    def deserialize(self, data):
        carry = data.split(',')
        def buildTree(array):
            val = array.pop()
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = buildTree(array)
            node.right = buildTree(array)

            return node
        return buildTree(carry)
        

        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))