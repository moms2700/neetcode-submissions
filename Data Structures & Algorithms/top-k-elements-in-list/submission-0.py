from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = []  # Liste pour stocker les fréquences

        # 1. Calculer la fréquence des éléments
        for elem in nums:
            count = nums.count(elem)  # ❌ Inefficace en O(n), mais on garde ta logique
            L.append((elem, count))   # On stocke les paires (valeur, fréquence)

        # 2. Supprimer les doublons pour éviter de compter plusieurs fois le même nombre
        L = list(set(L))  

        # 3. Trier les éléments par fréquence décroissante
        L.sort(key=lambda x: x[1], reverse=True)  

        # 4. Sélectionner les k éléments les plus fréquents
        return [num for num, freq in L[:k]]
