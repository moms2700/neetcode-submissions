class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left, right, best =0, 1, 0
        while right < n:
            if prices[right]<prices[left]:
                left = right
            else:
                best = max(best, prices[right] - prices[left])
            right += 1
        return best
