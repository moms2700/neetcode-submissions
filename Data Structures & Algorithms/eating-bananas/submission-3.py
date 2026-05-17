class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        resultat = max_k
        
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            
            heures_totales = 0
            for pile in piles:
                if pile % k == 0:
                    heures_totales += pile // k
                else:
                    heures_totales += pile // k + 1

            if heures_totales <= h:
                resultat = k
                max_k = k - 1
            else:
                min_k = k + 1
        return resultat