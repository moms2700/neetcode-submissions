# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q: 
                return False
            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return False
        if isSameTree(root, subRoot):
            return True
        
        gauche = self.isSubtree(root.left, subRoot)
        droite = self.isSubtree(root.right, subRoot)
        return droite or gauche 

            
        
            
        