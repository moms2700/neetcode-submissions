# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0        
        gauche = self.maxDepth(root.left)        
        droite = self.maxDepth(root.right)        
        return max(gauche, droite) + 1
        