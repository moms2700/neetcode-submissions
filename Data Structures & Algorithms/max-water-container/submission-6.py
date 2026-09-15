class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        res = 0

        while i < j:
            val = min(heights[j],heights[i]) * (j-i)
            res = max(res, val)
            if heights[i]<= heights[j]:
                i += 1
            else :
                j -= 1
            
        return res


