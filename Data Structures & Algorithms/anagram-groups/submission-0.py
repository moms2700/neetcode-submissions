class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a, b = sorted(s), sorted(t)  

        for i in range(len(a)):  
            if a[i] != b[i]:
                return False
        
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = []  # Liste pour stocker les groupes d'anagrammes
        visited = set()  # Ensemble pour éviter les répétitions

        for i in range(len(strs)):  # Parcours chaque mot de la liste
            if strs[i] in visited:
                continue  # Évite d'ajouter un mot déjà traité
            
            group = [strs[i]]  # Crée un groupe pour cet anagramme
            visited.add(strs[i])

            for j in range(i + 1, len(strs)):  # Vérifie les autres mots
                if self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited.add(strs[j])  # Marque comme traité

            L.append(group)  # Ajoute le groupe à la liste principale
        
        return L