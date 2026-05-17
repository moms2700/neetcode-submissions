class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        gauche = self.maxDepth(root.left)
        
        droite = self.maxDepth(root.right)
        
        return max(gauche, droite) + 1