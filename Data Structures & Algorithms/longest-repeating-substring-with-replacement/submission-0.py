class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_freq = 0
        resultat = 0
        gauche = 0
        compteur = {} 
        
        for droite in range(n): 
            compteur[s[droite]] = compteur.get(s[droite], 0) + 1
            
            max_freq = max(max_freq, compteur[s[droite]])
            
            while (droite - gauche + 1) - max_freq > k:  
                compteur[s[gauche]] -= 1  
                gauche += 1  
            
            resultat = max(resultat, droite - gauche + 1)  
        
        return resultat  