from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialisation avec des 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:  # Trouver le premier jour plus chaud
                    result[i] = j - i  # Calcul du nombre de jours à attendre
                    break  # Sortir dès qu'on trouve un jour plus chaud

        return result
