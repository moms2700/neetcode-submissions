class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Convertir en minuscules et supprimer les caractères non alphanumériques
        s = ''.join(char.lower() for char in s if char.isalnum())

        # 2. Vérifier si la chaîne est un palindrome en comparant les extrémités
        milieu = len(s) // 2
        for i in range(milieu):
            if s[i] != s[-(i + 1)]:  # Comparaison symétrique
                return False
        
        return True  # Si aucune différence n'a été trouvée, c'est un palindrome
