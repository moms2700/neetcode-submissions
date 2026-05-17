class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
                return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1
        while left <= right:
            milieu = (left + right) // 2
            milieu_valeur = matrix[milieu // n][milieu % n]
            if milieu_valeur == target:
                return True
            elif milieu_valeur < target:
                left = milieu + 1
            else:
                right = milieu - 1
        return False
                    