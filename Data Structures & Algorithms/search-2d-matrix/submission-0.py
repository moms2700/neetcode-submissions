from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Vérifier si la matrice est vide
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # Indices pour la recherche binaire

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)  # Trouver la position dans la matrice
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1  # Aller vers la droite
            else:
                right = mid - 1  # Aller vers la gauche

        return False