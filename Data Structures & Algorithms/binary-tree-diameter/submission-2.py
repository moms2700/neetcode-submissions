# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diametre = 0
        def calculer_hauteur(noeud):
            if not noeud:
                return 0
            hauteur_gauche = calculer_hauteur(noeud.left)
            hauteur_droite = calculer_hauteur(noeud.right)
            self.max_diametre = max(self.max_diametre, hauteur_gauche + hauteur_droite)           
            return 1 + max(hauteur_gauche, hauteur_droite)
        calculer_hauteur(root)
        return self.max_diametre
        