# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        resultat = []
        file = deque([root]) # On commence avec la racine
        
        while file:
            niveau_actuel = []
            taille_du_niveau = len(file) # Combien de nœuds à cet étage ?
            
            for i in range(taille_du_niveau):
                noeud = file.popleft() # On sort le premier de la file
                niveau_actuel.append(noeud.val)
                
                # On prépare le niveau suivant en ajoutant les enfants
                if noeud.left:
                    file.append(noeud.left)
                if noeud.right:
                    file.append(noeud.right)
            
            resultat.append(niveau_actuel) # On a fini un étage !
            
        return resultat