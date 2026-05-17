from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resultats = []
        for taille in range(len(t), len(s) + 1):
            for start in range(len(s) - taille + 1):
                resultats.append(s[start:start + taille])
        
        for elem in resultats:
            t_count = Counter(t)
            elem_count = Counter(elem)
            if all(elem_count[char] >= t_count[char] for char in t_count):
                return elem
        return ""