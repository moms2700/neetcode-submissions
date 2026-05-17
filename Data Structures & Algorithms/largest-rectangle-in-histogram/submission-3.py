class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            h = heights[i]

            gauche = i

            while gauche > 0 and heights[gauche - 1] >= h:
                gauche -= 1
            
            droit = i
            while droit < n - 1 and heights[droit + 1] >= h:
                droit += 1
            
            largeur = droit - gauche + 1
            aire = h * largeur
            max_area = max(max_area, aire)
        
        return max_area