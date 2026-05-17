class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        g, d = 0, n-1
        while g<d:
            cal = (d-g)*min(heights[d],heights[g])
            res = max(cal,res)
            if heights[g] <= heights[d]:
                g+=1
            else:
                d-=1
        return res

        