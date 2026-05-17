# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        def hauteur(nods):
            if not nods:
                return 0        
            gauche = hauteur(nods.left)        
            droite = hauteur(nods.right)        
            return max(gauche, droite) + 1
        if abs(hauteur(root.left) - hauteur(root.right)) <= 1:
            gogo = self.isBalanced(root.left)
            dodo = self.isBalanced(root.right)
            return gogo and dodo 
        return False
        
