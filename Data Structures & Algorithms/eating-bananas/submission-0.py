import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Trouve la vitesse minimale k à laquelle Koko peut manger toutes les bananes.
        """

        low = 1
        high = max(piles)
        min_k = high 
        while low <= high:
            k_candidate = low + (high - low) // 2
            if k_candidate == 0:
                low = 1
                continue
            hours_needed = 0
            for pile_size in piles:
                hours_needed += math.ceil(pile_size / k_candidate)

            if hours_needed <= h:
                min_k = k_candidate
                high = k_candidate - 1
            else:
                low = k_candidate + 1

        return min_k