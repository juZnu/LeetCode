class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if right:
            return f"{root.val}({left})({right})"
        if left:
            return f"{root.val}({left})"
        return f"{root.val}"
        